import pygame
from level import Level
from pytmx.util_pygame import load_pygame
from ui import Caption


class Tutorial(Level):
    def __init__(self, pause, start_game):
        self.start_game = start_game

        tmx_data = load_pygame('../data/tutorial.tmx')
        super().__init__(pause, tmx_data=tmx_data)

        self.raining = False
        self.soil_layer.raining = self.raining

        self.steps = ['Use WASD or the arrow keys to move',
                      'Use Q to change tools, \nsee bot left corner',
                      'You can press SPACE to use your tools, \nTake the hoe and use space to plow the ground',
                      'Use E to change seeds, take the tomato seeds',
                      'Use CRTL to plant the tomato seed on the plowed ground',
                      "Take the watering can and water the tomato seeds, \nRemember, press SPACE to use tools\n Note: you don't need to water if it is raining",
                      "You'll need to wait till they grow, \nbut you can sleep to speed up the process\n Go up to your bed and press ENTER",
                      "The plant has grown a bit, \nRepeat the process until it is fully grown\n",
                      "You now can harvest it by running on it",
                      "The tutorial is complete!\nPress ENTER to start the game"]
        self.step_counter = 0
        self.current_step = self.steps[self.step_counter]
        self.caption = Caption(text=self.current_step)

        # step 0:
        self.right = False
        self.left = False
        self.up = False
        self.down = False

        # step 8:
        self.tomato_harvested = False

    def next_step(self):
        self.step_counter += 1
        if self.step_counter >= len(self.steps):
            self.start_game(self.player.name)
        else:
            self.current_step = self.steps[self.step_counter]
            self.caption = Caption(text=self.current_step)

    def check_move(self):
        if self.player.direction.x > 0:
            self.right = True
        elif self.player.direction.x < 0:
            self.left = True
        if self.player.direction.y > 0:
            self.up = True
        elif self.player.direction.y < 0:
            self.down = True

        if self.right and self.left and self.up and self.down:
            self.next_step()

    def check_tools_switch(self):
        if self.player.selected_tool == 'water':
            self.next_step()

    def check_plowing(self):
        if len(self.soil_layer.soil_sprites) > 0:
            self.next_step()

    def check_tomato_seeds(self):
        if self.player.selected_seed == 'tomato':
            self.next_step()

    def check_planting(self):
        for plant in self.soil_layer.plant_sprites:
            if plant.plant_type == 'tomato':
                self.next_step()

    def check_watering(self):
        if not self.raining:
            for plant in self.soil_layer.plant_sprites:
                if plant.plant_type == 'tomato':
                    watered = plant.check_watered(plant.rect.center)
                    if watered:
                        self.next_step()

    def check_sleep(self):
        if self.player.sleep:
            self.next_step()

    def check_harvestable(self):
        for plant in self.soil_layer.plant_sprites:
            if plant.harvestable:
                if plant.plant_type == 'tomato':
                    self.next_step()

    def check_harvested(self):
        if self.tomato_harvested:
            self.next_step()

    def check_enter(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.next_step()

    def player_add(self, item):
        super().player_add(item)
        if item == 'tomato':
            self.tomato_harvested = True

    def run(self, dt):
        super().run(dt)
        self.caption.draw(self.display_surface)
        if self.step_counter == 0:
            self.check_move()
        elif self.step_counter == 1:
            self.check_tools_switch()
        elif self.step_counter == 2:
            self.check_plowing()
        elif self.step_counter == 3:
            self.check_tomato_seeds()
        elif self.step_counter == 4:
            self.check_planting()
        elif self.step_counter == 5:
            self.check_watering()
        elif self.step_counter == 6:
            self.check_sleep()
        elif self.step_counter == 7:
            self.check_harvestable()
        elif self.step_counter == 8:
            self.check_harvested()
        elif self.step_counter == 9:
            self.check_enter()