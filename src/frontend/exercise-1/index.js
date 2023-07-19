(() => {
  const $pixiContainer = document.getElementById("pixi-container");

  const app = new PIXI.Application({
    background: "#1099bb",
    resizeTo: $pixiContainer,
  });

  $pixiContainer.appendChild(app.view);

  // create a new Sprite from an image path
  const bunny = PIXI.Sprite.from("https://pixijs.com/assets/bunny.png");

  // move the sprite to the center of the screen
  bunny.x = app.screen.width / 2;
  bunny.y = app.screen.height / 2;

  app.stage.addChild(bunny);

  const targetX = bunny.x + 100;
  const targetY = bunny.y + 100;

  // animate sprite moving right and down
  const animate = () => {
    if (bunny.x < targetX) {
      bunny.x += 1;
    } else if (bunny.y < targetY) {
      bunny.y += 1;
    }
  };

  app.ticker.add(animate);
})();
