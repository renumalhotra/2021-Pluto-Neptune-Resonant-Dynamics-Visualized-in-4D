This GitHub directory contains the python code used to generate rotating frame plots and animations to visualize the orbital evolution of the Pluto-Neptune mean motion resonance in 3D+time. With a few small changes, this code can be used to study other MMR systems. The contents of this directory are as follows

- 3body.py : this python script is used to integrate (with the orbit integrator, REBOUND) the 3 body problem of the Sun, Neptune, and Pluto. The inputs are downloaded by the script from JPL-Horizons. The outputs from this script are: (i) a text file ('rebound_data.txt') containing the time history (at intervals of 5 years) of the cartesian coordinates (both rotated and non-rotated) of Neptune and Pluto; and (ii) static plots of the orbits traced in the rotating frame, projected in (x,y) (y,z) (x,z) and (x,y,z) (in './Examples/plots/')

- make_frames.py : this python script reads in the data from 'rebound_data.txt' and creates individual frames in a sequence of time steps as the bodies move along their orbits, as  traced in the rotating frame. These frames are saved to the subdirectory '/tmp_frames'

- animator.py : this python script reads in the frames from /tmp_frames and outputs an animation (in mp4 format) of the orbits as traced in the rotating frame; the animation files are saved to the main directory. This script also deletes the contents of /tmp_frames once the animation is saved

- tmp_frames : the subdirectory where animation frames are temporarily stored

- rebound_data.txt : this text file contains the time history of the rotated and non-rotated cartesian coordinates for the 3 body model, integrated in 3body.py

- Examples : this subdirectory contains example plots and animations for the Pluto-Neptune system visualized in (x,y) (y,z) (x,z) and (x,y,z) in the rotating frame of Neptune. there are also example plots for a nearby non-MMR case where Pluto's initial semi major axis was increased by 1% to shift it out of MMR

Reference: Zaveri and Malhotra (2021), Visualizing Pluto's Orbit in 4D, 52nd Annual meeting of the AAS-DDA, Poster #107-02
