
## Preparation of Input Files for MD simulation

# 1. Generate topology files using pdb2gmx
# The purpose of pdb2gmx is to generate three files:
#               1. The post-processed structure file (*.gro)
#               2. The topology file containing all the necessary information for defining a molecule, i.e., the bonded and the non-bonded parameters (topol.top).
#               3. A position restrained file (porse.itp)
## After execution of this command you will be prompted to choose a force-field, water model, protonation states of the ionizable amino acids and states of the N- and C- termini.

gmx pdb2gmx -f protein.clean.pdb -o protein.gro -inter -ignh


# 2. Define Box and Solvate using editconf

gmx editconf -f protein.gro -o protein.box.gro -c -d 1.5 -bt cubic

gmx solvate -cp protein.box.gro -cs spc216 -o protein.solv.gro


# 3. Add Ions

gmx grompp -f ions.mdp -c protein.solv.gro -p topol.top -o ions.tpr

gmx genion -s ions.tpr -p topol.top -o protein.solv-ions.gro -pname NA -nname CL -conc 0.15 -neutral


## Running MD simulation

# Energy minimisation

gmx grompp -f min.mdp -c protein.solv-ions.gro -p topol.top -o min.tpr

gmx mdrun -s min.tpr -deffnm min -v -ntomp 1


# NVT equilibration

gmx grompp -f nvt.mdp -c min.gro -r min.gro -p topol.top -o nvt.equi.tpr

gmx mdrun -s nvt.equi.tpr -deffnm nvt

# NPT equilibration

gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.equi.tpr

gmx mdrun -s npt.equi.tpr -deffnm npt

# Production run

gmx grompp -f npt.prod.mdp -c npt.gro -t npt.cpt -p topol.top -o npt.prod.tpr

gmx mdrun -s npt.prod.tpr -deffnm md_100ns


## Analysis

# Trajectory Post-processing

gmx trjconv -s npt.prod.tpr -f md_100ns.xtc -o md_noPBC.xtc -pbc mol -center

# RMSD

gmx rms -s npt.prod.tpr -f md_noPBC.xtc -o rmsd.xvg -tu ns

# Radius of Gyration

gmx gyrate -s npt.prod.tpr -f md_noPBC.xtc -o gyrate.xvg


# RMSF

gmx rmsf -s npt.prod.tpr -f md_noPBC.xtc -o rmsf.xvg -n protein.ndx -res






