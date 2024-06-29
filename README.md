# Nuke-SmoothScrub

Performance hack: it plays at 0 fps while scrubbing, which can be a lot smoother than normal viewer scrubbing.
And it also allows viewer scrubbing by clicking anywhere in the viewer instead of on the timeline. Feels nicer.
<br><br>

### Toggle: `ctrl+space` in viewer (can be changed in `menu.py`!)

---

## Performance Hack

In order for the 'performance hack' to work, the frames you're scrubbing through must be cached already.  
Often, even cached frames are laggy in Nuke when scrubbing through them.
<br>But somehow, that's not the case when playing the shot - so this script plays the active viewer at 0 fps, which makes the scrubbing much smoother.

![Nuke Smooth Scrubbing Viewer Laggy](https://maxvanleeuwen.com/wp-content/uploads/SmoothScrub_comparison.gif)

---

## Scrubbing from Anywhere in the Viewer

When SmoothScrub is on, you can click+drag from anywhere in the viewer like in many image playback softwares (instead of only dragging in the timeline).

---

### Individual features can be disabled in the `menu.py`.  
Works with Nuke 11 and 12, in <10 only the smooth scrubbing works.

---

## Installation:

1. Place the SmoothScrub folder in your `.nuke` folder (or somewhere else on your computer)
2. Go to your `.nuke` folder, and create a file called `init.py`. If such a file already exists, open it.
3. In the `init.py` file, add this line of text to the end and save it:
    ```python
    nuke.pluginAddPath('./SmoothScrub')
    ```
    If you want to place the folder somewhere else than in the `.nuke` folder, make sure to change the path in the `init.py` file so that it points to that other path instead!

---

## Installation using NukeShared

1. Place the SmoothScrub folder in the `_AutoInstaller` repository.

NukeShared is a way of installing plugins by dragging/dropping them in folders, [see my website](https://maxvanleeuwen.com/nukeshared) for more information.
