# imports
import random
import os
import subprocess
import time

# Constants

TEXT_FILE_PATH = "text.txt"

COAUTHOR_1 = "Co-authored-by: @patriciahopatriciaos7217-eng <patriciahopatriciaos7217@gmail.com>"
COAUTHOR_2 = "Co-authored-by: @babumahir655 <babumahir655@gmail.com>"
COAUTHOR_3 = "Co-authored-by: @n0 <luke@u.software>"

COMMIT_MESSAGE = f"""
Added a small change to {TEXT_FILE_PATH}


{COAUTHOR_1}
{COAUTHOR_2}
{COAUTHOR_3}"""

# First Make a new branch with a meaningful name that dont looks like its a random branch

def gen_branch_name():
    # get a dictionary of words
    word_1 = [
        # celestial / cosmic bodies
        "space", "moon", "star", "planet", "galaxy", "universe", "comet",
        "asteroid", "meteor", "meteorite", "constellation", "asteroid-belt",
        "solar-system", "exoplanet", "gas-giant", "dwarf-planet", "satellite",
        # exotic objects / phenomena
        "black-hole", "wormhole", "nebula", "quasar", "pulsar", "supernova",
        "dark-matter", "dark-energy", "light-year", "singularity",
        "event-horizon", "multiverse", "parallel-universe", "cosmos", "void",
        "interstellar", "deep-space", "space-time", "dimension",
        # physics / science
        "gravity", "orbit", "time", "energy", "matter", "radiation", "photon",
        "neutrino", "atom", "molecule", "particle", "quark", "electron",
        "proton", "neutron", "plasma", "vacuum", "entropy", "relativity",
        "thermodynamics", "cosmology", "astrophysics", "astrobiology",
        # astronomy / observation
        "telescope", "observatory", "eclipse", "equinox", "solstice", "aurora",
        "meteor-shower", "solar-wind", "cosmic-ray", "gamma-ray",
        # life / intelligence / tech
        "extraterrestrial", "alien", "lifeform", "intelligence", "civilization",
        "technology", "robotics", "artificial-intelligence", "machine-learning",
        "neural-network", "quantum-computing",
        # travel / vessels
        "astronaut", "cosmonaut", "taikonaut", "spaceship", "starship",
        "spacecraft", "warp-drive", "hyperdrive", "probe", "rover", "lander",
        "module", "space-station", "moonbase", "colony", "outpost",
        # abstract / boundary
        "frontier", "horizon", "zenith", "nadir",
    ]

    word_2 = [
        # exploration missions
        "exploration", "discovery", "adventure", "journey", "mission",
        "expedition", "voyage", "quest", "odyssey", "pilgrimage", "safari",
        "crusade", "trek", "sojourn", "wanderlust", "traverse", "crossing",
        "navigation", "pioneering", "pathfinding", "scouting", "seeking",
        "searching", "probing", "surveying", "mapping", "charting", "survey",
        "scan", "sweep", "patrol", "pursuit", "chase", "race", "dash", "sprint",
        "marathon", "relay",
        # motion / movement
        "roaming", "traveling", "wandering", "drifting", "floating", "gliding",
        "soaring", "flying", "hovering", "levitating", "ascending", "descending",
        "climbing", "scaling", "mountaineering", "launch", "ascent", "descent",
        "landing", "docking", "orbit", "flyby", "encounter", "rendezvous",
        # operations
        "contact", "signal", "transmission", "broadcast", "uplink", "downlink",
        "telemetry", "observation", "analysis", "study", "research",
        "experiment", "investigation", "sampling", "collection", "gathering",
        "assembly", "synthesis", "formation", "creation", "construction",
        "fabrication", "operation",
    ]

    word_3 = [
        # explorers / travelers
        "explorer", "adventurer", "traveler", "wanderer", "nomad", "pilgrim",
        "journeyman", "wayfarer", "roamer", "drifter", "globetrotter", "voyager",
        "pioneer", "trailblazer", "pathfinder", "navigator", "scout", "seeker",
        "quester", "expeditionist", "explorator", "discoverer",
        # researchers / intellectuals
        "investigator", "researcher", "scientist", "scholar", "academic",
        "intellectual", "thinker", "philosopher", "theorist", "visionary",
        "futurist", "innovator", "inventor", "analyst", "observer",
        "astronomer", "astrophysicist", "cosmologist", "physicist",
        "mathematician", "chemist", "biologist", "geologist", "meteorologist",
        # makers / doers
        "creator", "artist", "designer", "engineer", "architect", "builder",
        "maker", "craftsman", "technician", "specialist", "expert",
        "programmer", "developer", "coder", "mechanic", "technologist",
        # space crew
        "astronaut", "cosmonaut", "taikonaut", "pilot", "captain", "commander",
        "officer", "crew", "operator",
        # leaders / mythic
        "strategist", "planner", "coordinator", "director", "manager", "leader",
        "chief", "master", "guru", "sage", "oracle", "prophet", "herald",
        "guardian", "sentinel", "watchman", "knight", "warrior", "champion",
        "hero", "legend", "myth",
    ]
    
    # generate a random number of 4 digits
    
    suffix = random.randint(10000, 99999)
    
    # generate a random word with the first, secon, and third word and the suffix
    branch_name = f"{random.choice(word_1)}-{random.choice(word_2)}-{random.choice(word_3)}-{suffix}"
    
    return str(branch_name)

#  Now create a branch with that name
def create_branch(branch_name):
    # check if the branch already exists
    branches = subprocess.check_output(["git", "branch"]).decode("utf-8").split("\n")
    if branch_name in branches:
        print(f"Branch {branch_name} already exists")
        return False
    
    # create the branch
    subprocess.call(["git", "checkout", "-b", branch_name])
    print(f"Branch {branch_name} created")
    return True

# create a function to switch to a specific branch
def switch_branch(branch_name):
    # check if the branch exists
    branches = subprocess.check_output(["git", "branch"]).decode("utf-8").split("\n")
    if branch_name not in branches:
        print(f"Branch {branch_name} does not exist")
        return False
    
    # switch to the branch
    subprocess.call(["git", "checkout", branch_name])
    print(f"Switched to branch {branch_name}")
    return True

# a function to run a command in the terminal and also print the output
def run_command(command):
    # run the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # print the output
    print(result.stdout)
    
    # check if there was an error
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    
    return True

# create a function to create a file with the name text.txt
def create_file(file_path):
    # check if the file already exists
    if os.path.exists(file_path):
        print(f"File {file_path} already exists")
        return False
    
    # create the file
    with open(file_path, "w") as f:
        f.write("This is a test file")
    
    print(f"File {file_path} created")
    return True

# make a function to add a small change to the text file
def add_change_to_text_file(file_path):
    # check if the file exists
    create_file(file_path)

    # add a small change to the file
    with open(file_path, "a") as f:
        f.write("\nThis is a small change")
    
    print(f"Small change added to {file_path}")
    return True


def main():
    # generate a branch name
    branch_name = gen_branch_name()
    
    # create the branch
    create_branch(branch_name)

    
    # add a small change to the text file
    add_change_to_text_file(TEXT_FILE_PATH)
    
    # add the file to git
    run_command("git add .")
    
    # commit the changes with a message
    subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True)
    
    # push the changes to the remote repository
    run_command(f"git push origin {branch_name}")
    
    # create a pull request with the changes to the new branch and the main branch
    run_command(f'gh pr create --base main --head {branch_name} --fill')
    
    #  merge the pull request
    run_command(f'gh pr merge {branch_name} --squash')
    
    run_command("git checkout main")

if __name__ == "__main__":
    loopturns = int(input("How many times do you want to run the script? "))
    # time delay to prevent rate limiting max 100 seconds
    time_delay = int(input("How long do you want to wait between runs? (in seconds) "))
    if time_delay < 100:
        time_delay = 100
    for i in range(loopturns):
        main()
        print(f"Finished run {i+1} of {loopturns}")
        if i < loopturns - 1:
            print(f"Waiting {time_delay} seconds before next run")
            time.sleep(time_delay)