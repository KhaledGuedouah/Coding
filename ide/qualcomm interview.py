
uint8_t var ;
# 5eme 6eme bit 
uint8_t var2 =  0b000000xx
# ecrire xx dans 5eme et 6eme bit de Var 
def fun (var, var2) : 
    return ((var & ~(3<<5))| var2<<5)
# qualcomm 
# list de tous les fichier qui contiennet "Task"
cd qualcomm 
grep -rl "Task" --include = "*.py"

find -type f -name = "toto*.py" -exec grep -rl "task" {} +  

find -type f -name="*.py" | xargs grep -l "Task" # xargs for pipe to apply on all the files on the generated output 

pd aux | grep ="python"

git fetch origin 
git status 
git merge 
git add toto.py # stage 
git commit -m "toto method implemeted"

git reset -- hard toto.py # unstage 
gh pr 


 