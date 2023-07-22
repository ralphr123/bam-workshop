import { callBackend } from "../_lib/callBackend.js";
import { Maze } from "../_lib/maze.js";
import { handleRunTests } from "../_lib/handleRunTests.js";

(async () => {
  const maze = new Maze({
    mazeDimensions: 8,
    spriteImageUrl: "https://pixijs.com/assets/bunny.png",
    elementIdToInject: "pixi-container",
  });

  // Put maze code inside plaque
  document.getElementById("maze-code-plaque").innerText = maze.mazeCode;

  const $sendBtn = document.getElementById("send-btn");
  const $input = document.getElementsByTagName("input")[0];
  const $responseArea = document.getElementById("response-area");

  $input.value = maze.mazeCode;

  $sendBtn.addEventListener("click", send);

  async function send() {
    // Fetch exercise data
    const data = await callBackend({
      path: `/exercise4/${encodeURIComponent(maze.mazeCode)}`,
    });

    const instructions = data?.instructions;

    if (!instructions?.length) return;

    // Follow recieved maze instructions
    for (const instruction of instructions) {
      $responseArea.innerText += instruction + "\n";
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
  }

  handleRunTests("exercise4");
})();
