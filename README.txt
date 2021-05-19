This GitHub directory contains the python code used to generate plots and animations to visualize the orbital evolution of the Pluto-Neptune mean motion resonance (MMR) in 3D+time. This visualization is made in a frame rotating with the time-averaged orbital angular velocity of Neptune. With a few small changes, this code can be used to study other MMR systems. The contents of this directory are as follows

- 3body.py : this python script is used to integrate the 3 body problem of the Sun, Neptune, and Pluto (with the orbit integrator WHFAST in REBOUND, see https://github.com/hannorein/rebound). The inputs are downloaded by the script from JPL-Horizons. The outputs from this script are: (i) a text file ('rebound_data.txt') containing the time history (at intervals of 5 years) of the cartesian coordinates (both rotated and non-rotated) of Neptune and Pluto; and (ii) static plots of the orbits traced in the rotating frame, projected in (x,y) (y,z) (x,z) and (x,y,z) (in './Examples/plots/')

- make_frames.py : this python script reads in the data from 'rebound_data.txt' and creates individual frames in a sequence of time steps as the bodies move along their orbits, as  traced in the rotating frame. The user must specify -- in line 114 of make_frames.py -- which projection to make [e.g., fig1 = plotter_yz(i)]. These frames are saved to the subdirectory '/tmp_frames'

- animator.py : this python script reads in the frames from /tmp_frames and outputs an animation (in mp4 format) of the orbits as traced in the rotating frame; the animation files are saved to the main directory. (On line 12 of animator.py, be sure to change the filename when running a new animation to avoid overwriting files.) This script also deletes the contents of /tmp_frames once the animation is saved

- tmp_frames : the subdirectory where animation frames are temporarily stored

- rebound_data.txt : this text file contains the time history of the rotated and non-rotated cartesian coordinates for the 3 body model, integrated in 3body.py

- Examples : this subdirectory contains example plots and animations for the Pluto-Neptune system visualized in (x,y) (y,z) (x,z) and (x,y,z) in the rotating frame of Neptune. 

Reference: Zaveri and Malhotra (2021), Visualizing Pluto's Orbit in 4D, 52nd Annual meeting of the AAS-DDA, Poster #107-02
