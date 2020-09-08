# Mike Tyson's Punch-Out! Gym Retro Environment

> THIS IS A WORK IN PROGRESS.

An environment implementation for Mike Tyson's Punch-Out! (1987) of NES for Gym
Retro.

## Installation

To create a gym retro environment, you should probably start with their
[Getting Started Guide](https://retro.readthedocs.io/en/latest/getting_started.html).

In the root of this project, add your copy of Mike Tyson's Punch-Out! ROM
as `rom.nes` and it's `rom.sha` file.

Then, use the import script to register the game:

```
python -m retro.import /path/to/your/ROMs/directory/
```

For further information, please refer to Gym Retro's [Game Integration](https://retro.readthedocs.io/en/latest/integration.html) docs.

## LICENSE

This is free software, distributed under the terms of the GNU General Public
License as published by the Free Software Foundation, version 3 of the License
(or any later version). For more information, see the [LICENSE](LICENSE) file.
