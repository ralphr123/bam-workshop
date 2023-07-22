import { callBackend } from "../_lib/callBackend.js";
import { Maze } from "../_lib/maze.js";

(async () => {
  const maze = new Maze({
    mazeDimensions: 8,
    spriteImageUrl: "https://pixijs.com/assets/bunny.png",
    elementIdToInject: "pixi-container",
  });

  // Put maze code inside plaque
  document.getElementById("maze-code-plaque").innerText = maze.mazeCode;

  // Handles play and reset for students
  const $playBtn = document.getElementById("play-btn");

  // Save play button content
  const _playContent = $playBtn.innerHTML;
  const _loadingContent =
    '<img src="../static/assets/icons/gear.svg" class="rotating" />';
  const _resetContent =
    '<img src="../static/assets/icons/reset.svg" /><div>Reset</div>';

  let status = "ready";

  $playBtn.addEventListener("click", () => {
    if (status === "ready") play();
    if (status === "ended") reset();
  });

  async function play() {
    status = "active";

    // Replace play button content with rotating gear icon
    $playBtn.innerHTML = _loadingContent;

    // Fetch exercise data
    const data = await callBackend({
      path: `exercise4/${encodeURIComponent(maze.mazeCode)}`,
    });

    const instructions = data?.instructions;

    if (!instructions?.length) return;

    // Follow recieved maze instructions
    for (const instruction of instructions) {
      const instructionFragments = instruction.split(" ");

      if (instructionFragments.length !== 4) {
        continue;
      }
      const [, direction, steps] = instructionFragments;

      switch (direction) {
        case "RIGHT":
          await maze.moveSpriteX(Number(steps));
          break;
        case "LEFT":
          await maze.moveSpriteX(-Number(steps));
          break;
        case "UP":
          await maze.moveSpriteY(-Number(steps));
          break;
        case "DOWN":
          await maze.moveSpriteY(Number(steps));
          break;
      }
    }

    // Restore content of play button
    $playBtn.innerHTML = _resetContent;

    status = "ended";
  }

  function reset() {
    maze.resetSprite();
    status = "ready;";
    $playBtn.innerHTML = _playContent;
  }
})();
