import { Maze } from "../_lib/maze.js";

(async () => {
  const maze = new Maze({
    mazeDimensions: 4,
    spriteImageUrl: "https://pixijs.com/assets/bunny.png",
    elementIdToInject: "pixi-container",
  });

  // await maze.moveSpriteX(2);
  // await maze.moveSpriteY(1);
  // await maze.moveSpriteX(1);
})();

// Image by <a href="https://www.freepik.com/free-vector/flat-character-animation-frames_13818858.htm#page=2&query=sprites&position=49&from_view=keyword&track=sph">Freepik</a>
