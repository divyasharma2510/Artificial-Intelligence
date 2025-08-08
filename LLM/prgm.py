import random

def llm(prompt):
    print("LLM Prompt >>",prompt)
    if "next task" in prompt:
        return "search_for_information"
    elif "Did the task succeed" in prompt:
        return random.choice(["yes", "no"])
    elif "search_for_information" in prompt:
        return "I found some useful articles"
    elif "replan" in prompt:
        return "try_different_query"
    else:
        return "Task Completed"

class Memory:
    def __init__(self):
        self.logs = []
    def store(self, entry):
        self.logs.append(entry)
    def recall(self):
        return "\n".join(self.logs[-5:])


#Tools/Actions
class Tools:
    def search_for_information(self, query):
        return f"[Tool] Searching for '{query}'......"

    def try_different_query(self):
        return f"[Tool] Trying Alternative"


#Evaluator/Critic
class Critic:
    def evaluate(self, res):
        return llm(f"Did the task succeed?\nRe")
    
class Planner:
    def decide_next_task(self, goal, memeory):
        return llm(f"Given Goal: {goal} and Memory: {memeory}")
    
class Agent:
    def __init__(self, goal):
        self.goal = goal
        self.memory = Memory()
        self.tools = Tools()
        self.critic = Critic()
        self.planner = Planner()
    
    def run(self):
        for step in range(5):
            print(f"\n--- Step {step+1} ---")

            #Recall Memory
            mem = self.memory.recall()

            #Decide task using planner
            task = self.planner.decide_next_task(self.goal, self.memory)

            #the action method
            action = getattr(self.tools, task, None)

            if action:
                res = action(self.goal)
            else:
                res = llm(task)

            print(f"Task: {task}\nResult: {res}")
            self.memory.store(f"Task: {task}\nResult: {res}")

            #Evaluate Result
            success=self.critic.evaluate(res)
            print(f"Evaluation : {success}")
            self.memory.store(f"Evaluation: {success}")

            if success.lower() == "yes":
                print("Goal Achieved. Stopping.")
                break

if __name__=="__main__":
    agent = Agent(goal="Learn About Agentic Architectures")
    agent.run()

