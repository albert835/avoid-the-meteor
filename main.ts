namespace SpriteKind {
    export const enemy = SpriteKind.create()
    export const gas = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.gas, function (sprite, otherSprite) {
    statusbar.value = 100
    otherSprite.destroy(effects.spray, 500)
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    game.over(true, effects.clouds)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.enemy, function (sprite2, otherSprite2) {
    scene.cameraShake(4, 500)
    otherSprite2.destroy(effects.fire, 500)
    info.changeLifeBy(-1)
})
let myEnemy: Sprite = null
let myfuel: Sprite = null
let statusbar: StatusBarSprite = null
scene.setBackgroundImage(assets.image`Galaxy`)
scroller.scrollBackgroundWithSpeed(0, 10)
let mySprite = sprites.create(assets.image`Blue Rocket`, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
animation.runImageAnimation(
mySprite,
assets.animation`Flying Blue`,
200,
true
)
mySprite.setStayInScreen(true)
statusbar = statusbars.create(20, 4, StatusBarKind.Health)
statusbar.attachToSprite(mySprite, -30, 0)
game.onUpdateInterval(5000, function () {
    myfuel = sprites.createProjectileFromSide(assets.image`Fuel`, 0, 80)
    myfuel.x = randint(5, 155)
    myfuel.setKind(SpriteKind.gas)
})
game.onUpdateInterval(1000, function () {
    myEnemy = sprites.createProjectileFromSide(assets.image`Spider`, 0, 50)
    myEnemy.x = randint(5, 155)
    myEnemy.setKind(SpriteKind.enemy)
    animation.runImageAnimation(
    myEnemy,
    assets.animation`enemy`,
    100,
    true
    )
})
game.onUpdateInterval(1000, function () {
    info.changeScoreBy(10)
})
game.onUpdateInterval(300, function () {
    statusbar.value += -1
})
