class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                indegree[recipe] += 1
        
        recipes = set(recipes)
        queue = deque(supplies)
        cookable_foods = []

        while queue:
            food = queue.popleft()
            if food in recipes:
                cookable_foods.append(food)

            for made_food in graph[food]:
                indegree[made_food] -= 1
                if indegree[made_food] == 0:
                    queue.append(made_food)

        return cookable_foods

