# Max van Leeuwen - maxvanleeuwen.com
#
# SmoothScrub 1.0
# Change the parameters down below for customization!




# use smooth scrubbing (temporarily playing at 0fps)
useSmooth = True

# scrub only in timeline, as opposed to taking over mouse anywhere in viewer
timelineScrubOnly = False

# speed multiplier for scrubbing (1.0x = full frame range start-end in width of viewer)
scrubSpeed = 2.0

# keyboard shortcut
shortcutKey = "Ctrl+Space"




# load into nukeunder 'Viewer' right-click context
import SmoothScrub
nuke.menu('Viewer').addCommand('Smooth Scrub', lambda: SmoothScrub.SmoothScrub(useSmooth, timelineScrubOnly, scrubSpeed), shortcutKey)