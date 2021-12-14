# resolve-deliver-scripts
DaVinci Resolve deliver page render scripts

## Install
In powershell: 

```cd C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Deliver```

```git clone https://github.com/in03/resolve-deliver-scripts```

## Usage
1. In Resolve, open the 'deliver' page and open the 'render settings' panel
2. Click the 'video' tab, unfurl 'Advanced Settings' and scroll down to the bottom
3. Check the checkbox for 'Trigger script at __ of render job'
2. Choose `START` or `END` of render job
3. Choose the script you want to run

Scripts are prefixed with `START_` and `END_` respectively.
