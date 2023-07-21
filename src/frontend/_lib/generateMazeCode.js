import { Queue } from "./queue.js";

class CoordinateSet {
  /**
   *
   * @param {{ x: number; y: number }[]} arr
   */
  constructor(arr) {
    this.set = new Set();

    for (const coordinates of arr) {
      this.add(coordinates);
    }
  }

  /**
   *
   * @param {{ x: number; y: number }} coordinates
   * @returns {string} Hashed coordinates
   */
  hash({ x, y }) {
    return `${x}${y}`;
  }

  /**
   *
   * @param {{ x: number; y: number }} coordinates
   * @returns {Set<any>} Set
   */
  add(coordinates) {
    return this.set.add(this.hash(coordinates));
  }

  /**
   *
   * @param {{ x: number; y: number }} coordinates
   * @returns {boolean} - True if coordinates in set
   */
  has(coordinates) {
    return this.set.has(this.hash(coordinates));
  }
}

class MazeCode {
  constructor(instructions) {
    this.instructions = instructions || [];
  }

  /**
   *
   * @param {('U' | 'D' | 'L' | 'R')} direction
   */
  add(direction) {
    const newInstructions = this.instructions
      .slice()
      .map((instruction) => ({ ...instruction }));
    const prevInstruction = newInstructions[newInstructions.length - 1];

    if (prevInstruction?.direction === direction) {
      prevInstruction.steps += 1;
    } else {
      newInstructions.push({ direction, steps: 1 });
    }

    return new MazeCode(newInstructions);
  }

  /**
   *
   * @returns {string} String representation of maze instructions
   */
  toString() {
    let mazeCode = "\\instr";

    for (const { direction, steps } of this.instructions) {
      mazeCode += ` -${direction} ${steps}`;
    }

    return mazeCode;
  }
}

/**
 *
 * @param {number[][]} grid - nxn grid of numbers (1 = wall, 0 = path)
 * @returns {string} String representation of maze instructions
 *  - Every instruction starts with \instr. Following this are commands separated by single spaces.
 *  - Each of these commands take in one argument, being the distance travelled.
 *  - Here are the four commands (exluding the quotes):
 *  1. "-R <number>" = Go right <number> times
 *  2. "-L <number>" = Go left <number> times
 *  3. "-D <number>" = Go down <number> times
 *  4. "-U <number>" = Go up <number> times
 *  - Example command: "\instr -R 3 -D 2 -L 1 -U 1" (right 3 units, down two units, then left one unit)
 */
export function generateMazeCode(grid) {
  const startingCell = { x: 0, y: 1, path: new MazeCode() };
  const queue = new Queue(startingCell);
  const visited = new CoordinateSet([startingCell]);
  const size = grid.length;

  const isInBounds = ({ x, y }) =>
    x >= 0 && y >= 0 && x < size && y < size && grid[y][x] === 0;

  while (!queue.isEmpty()) {
    const { x, y, path } = queue.dequeue();

    if (x === size - 1 && y === size - 2) {
      return path.toString();
    }

    const cellAbove = { x, y: y - 1, path: path.add("U") };
    const cellBelow = { x, y: y + 1, path: path.add("D") };
    const cellLeft = { x: x - 1, y, path: path.add("L") };
    const cellRight = { x: x + 1, y, path: path.add("R") };

    if (isInBounds(cellAbove) && !visited.has(cellAbove)) {
      queue.enqueue(cellAbove);
      visited.add(cellAbove);
    }

    if (isInBounds(cellBelow) && !visited.has(cellBelow)) {
      queue.enqueue(cellBelow);
      visited.add(cellBelow);
    }

    if (isInBounds(cellLeft) && !visited.has(cellLeft)) {
      queue.enqueue(cellLeft);
      visited.add(cellLeft);
    }

    if (isInBounds(cellRight) && !visited.has(cellRight)) {
      queue.enqueue(cellRight);
      visited.add(cellRight);
    }
  }
}
