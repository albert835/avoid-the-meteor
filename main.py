@namespace
class SpriteKind:
    enemy = SpriteKind.create()
    gas = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    statusbar.value = 100
    otherSprite.destroy(effects.spray, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.gas, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    scene.camera_shake(4, 500)
    otherSprite2.destroy(effects.fire, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_on_zero(status):
    game.over(True, effects.clouds)
statusbars.on_zero(StatusBarKind.energy, on_on_zero)

myEnemy: Sprite = None
myfuel: Sprite = None
statusbar: StatusBarSprite = None
scene.set_background_image(assets.image("""
    Galaxy
"""))
scroller.scroll_background_with_speed(0, 10)
mySprite = sprites.create(assets.image("""
    Blue Rocket
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
animation.run_image_animation(mySprite,
    assets.animation("""
        Flying Blue
    """),
    200,
    True)
mySprite.set_stay_in_screen(True)
statusbar = statusbars.create(20, 4, StatusBarKind.health)
statusbar.attach_to_sprite(mySprite, -30, 0)

def on_update_interval():
    global myfuel
    myfuel = sprites.create_projectile_from_side(assets.image("""
        Fuel
    """), 0, 80)
    myfuel.x = randint(5, 155)
    myfuel.set_kind(SpriteKind.gas)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global myEnemy
    myEnemy = sprites.create_projectile_from_side(assets.image("""
        Spider
    """), 0, 50)
    myEnemy.x = randint(5, 155)
    myEnemy.set_kind(SpriteKind.enemy)
    animation.run_image_animation(myEnemy, assets.animation("""
        enemy
    """), 100, True)
game.on_update_interval(1000, on_update_interval2)

def on_update_interval3():
    info.change_score_by(10)
game.on_update_interval(1000, on_update_interval3)

def on_update_interval4():
    statusbar.value += -1
game.on_update_interval(300, on_update_interval4)
