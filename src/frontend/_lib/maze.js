import { generateMazeCode } from "./generateMazeCode.js";
import { generateRandomMaze } from "./generateRandomMaze.js";

export class Maze {
  /**
   *
   * @param {{ mazeDimensions: number; spriteImageUrl: string; elementIdToInject: string; }}
   */
  constructor({ mazeDimensions, spriteImageUrl, elementIdToInject }) {
    const $pixiContainer = document.getElementById(elementIdToInject);

    // Initialize instance of pixi app
    this.app = new PIXI.Application({
      background: "#1099bb",
      resizeTo: $pixiContainer,
    });

    // Generate random nxn matrix to represent maze
    this.grid = generateRandomMaze(mazeDimensions);

    // Generate maze code (string instruction set for correct path)
    this.mazeCode = generateMazeCode(this.grid);

    // Draw the maze on the app
    this.drawMaze();

    // Set sprite coordinates to maze entrance (starting cell)
    this.spriteCoordinates = { x: 0, y: 1 };

    // Generate pixi sprite with correct size and coordinates
    this.sprite = this.generateSprite(spriteImageUrl);

    // Add app to dom
    $pixiContainer.appendChild(this.app.view);
  }

  /**
   *
   * @param {string} url
   */
  generateSprite(url) {
    try {
      // Create a new Sprite from an image path
      const sprite = PIXI.Sprite.from(url);
      const cellSize = this.app.view.width / this.grid.length;

      // Set the sprite's size to fit within a cell
      sprite.height = cellSize;
      sprite.width = cellSize;

      // Move the sprite to initial position
      sprite.x = this.spriteCoordinates.x * cellSize;
      sprite.y = this.spriteCoordinates.y * cellSize;

      // Add sprite to dom
      this.app.stage.addChild(sprite);

      return sprite;
    } catch (e) {
      console.error("Error generating sprite:", e);
    }
  }

  drawMaze() {
    try {
      const cellSize = this.app.view.width / this.grid.length;

      for (let i = 0; i < this.grid.length; i++) {
        for (let j = 0; j < this.grid[i].length; j++) {
          const cell = this.grid[i][j];

          // Skip if empty path
          if (cell === 0) {
            continue;
          }

          const domCell = new PIXI.Graphics();

          let cellColor = "black";

          // Fill cell with correct color
          domCell.beginFill(cellColor);
          domCell.drawRect(0, 0, cellSize, cellSize);
          domCell.endFill();

          // Move cell to correct position
          domCell.x = j * cellSize;
          domCell.y = i * cellSize;

          // Add cell to app
          this.app.stage.addChild(domCell);
        }
      }
    } catch (e) {
      console.error("Error drawing maze:", e);
    }
  }

  /**
   *
   * @param {number} x - Horizontal grid index to move sprite to
   * @param {number} y - Vertical grid index to move sprite to
   * @returns {Promise<void>} Promise that resolves when motion is complete
   */
  moveSprite(x, y) {
    try {
      return new Promise((resolve) => {
        const cellSize = this.app.view.width / this.grid.length;
        const targetX = x * cellSize;
        const targetY = y * cellSize;

        // Callback to animate sprite's motion
        const animateMotion = () => {
          try {
            if (this.sprite.x < targetX) {
              this.sprite.x += 1;
            } else if (this.sprite.y < targetY) {
              this.sprite.y += 1;
            } else {
              this.app.ticker.remove(animateMotion);
              resolve();
            }
          } catch (e) {
            console.error("Error animating sprite motion", e);
            throw e;
          }
        };

        this.app.ticker.add(animateMotion);

        // Set new coordinates for sprite
        this.spriteCoordinates.x = x;
        this.spriteCoordinates.y = y;
      });
    } catch (e) {
      console.error("Error moving sprite:", e);
    }
  }

  /**
   *
   * @param {number} n - Number of cells to move sprite vertically (negative = up, positive = down)
   * @returns {Promise<void>} Promise that resolves when motion is complete
   */
  moveSpriteY(n) {
    return this.moveSprite(
      this.spriteCoordinates.x,
      this.spriteCoordinates.y + n
    );
  }

  /**
   *
   * @param {number} n - Number of cells to move sprite horizontally (negative = left, positive = right)
   * @returns {Promise<void>} Promise that resolves when motion is complete
   */
  moveSpriteX(n) {
    return this.moveSprite(
      this.spriteCoordinates.x + n,
      this.spriteCoordinates.y
    );
  }
}