#!/bin/env python

import pyglet

class Player():
	def main():
		play_clip('ng-engine_noise.wav')
		play_clip('tos-bridge.wav')
		play_clip('ng-theme.wav')

		pyglet.app.run()

	def play_clip(clip):
		sound = pyglet.resource.media(clip)
		player = pyglet.media.Player()
		player.volume = 1.0
		player.queue(sound)
		player.play()

if __name__== "__main__":
    main()