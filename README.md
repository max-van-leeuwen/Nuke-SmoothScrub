# Nuke-SmoothScrub

<p> </p>
<p>Viewer scrubbing by clicking anywhere in the viewer instead of on the timeline.</p>
<p>Also a performance hack: it plays at 0 fps while scrubbing, which can be a lot smoother than nomal viewer scrubbing.</p>
<p> </p>
<p>Toggle: ctrl+space in viewer (can be changed in menu.py!)</p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p><strong>Performance hack</strong></p>
<p>In order for the 'performance hack' to work, the frames you're scrubbing through must be cached already.<br />Often, even cached frames are laggy in Nuke when scrubbing through them. But not when playing the shot - so this script plays the active viewer at 0 fps, which makes the scrubbing much smoother.</p>
<p> </p>
<p> </p>
<p><img src="https://maxvanleeuwen.com/wp-content/uploads/SmoothScrub_comparison.gif" alt="nuke smooth scrubbing viewer laggy" /></p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p><strong>Scrubbing from anywhere in the viewer</strong></p>
<p> </p>
<p>When SmoothScrub is on, you can click+drag from anywhere in the viewer like in many image playback softwares (instead of only dragging in the timeline).</p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p><strong>Both the smooth scrubbing and the clicking anywhere in the viewer are enabled by default, but can be disabled individually in the menu.py.</strong></p>
<p>Works with Nuke 11 and 12, in &lt;10 only the smooth scrubbing works.</p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p><strong>Installation:</strong></p>
<p> </p>
<p>1. Place the SmoothScrub folder in your .nuke folder (or somewhere else on your computer)</p>
<p>2. Go to your .nuke folder, and create a file called 'init.py'. If such a file already exists, open it.</p>
<p>3. In the init.py file, add this line of text to the end and save it:</p>
<p>nuke.pluginAddPath('./SmoothScrub')</p>
<p> </p>
<p>If you want to place the folder somewhere else than in the .nuke folder, make sure to change the path in the init.py file so that it points to that other path instead!</p>
<p> </p>
<p> </p>
<p><strong>Installation using NukeShared</strong></p>
<p> </p>
<p>1. Place the SmoothScrub folder in the '_AutoInstaller' repository.</p>
<p> </p>
<p>NukeShared is a way of installing plugins by dragging/dropping them in folders, <a href="https://maxvanleeuwen.com/nukeshared" target="_blank">see my website (maxvanleeuwen.com/nukeshared)</a> for more information.</p>
