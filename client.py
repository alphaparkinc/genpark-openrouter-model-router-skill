class OpenRouterModelRouterClient:
    def route(self, task_complexity: str, max_cost_limit: float) -> dict:
        model = "anthropic/claude-3-opus" if task_complexity == "high" and max_cost_limit > 0.05 else "meta-llama/llama-3-70b-instruct"
        return {"selected_model": model}