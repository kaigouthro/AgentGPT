from typing import List, Optional, Protocol

from fastapi.responses import StreamingResponse as FastAPIStreamingResponse

from reworkd_platform.web.api.agent.analysis import Analysis


class AgentService(Protocol):
    async def start_goal_agent(self, *, goal: str) -> List[str]:
        pass

    async def analyze_task_agent(
        self, *, goal: str, task: str, tool_names: List[str]
    ) -> Analysis:
        pass

    async def execute_task_agent(
        self,
        *,
        goal: str,
        task: str,
        analysis: Analysis,
    ) -> FastAPIStreamingResponse:
        pass

    async def create_tasks_agent(
        self,
        *,
        goal: str,
        tasks: List[str],
        last_task: str,
        result: str,
        completed_tasks: Optional[List[str]] = None,
    ) -> List[str]:
        pass

    async def summarize_task_agent(
        self,
        *,
        goal: str,
        results: List[str],
    ) -> FastAPIStreamingResponse:
        pass

    async def chat(
        self,
        *,
        message: str,
        results: List[str],
    ) -> FastAPIStreamingResponse:
        pass

    async def evaluate_tasks(self, *, tasks: List[str], goal: str) -> List[str]:
        """
        Evaluate tasks against defined criteria and return a list of task IDs
        that should be updated or deleted.
        """
        # Logic to evaluate tasks based on criteria
        evaluated_tasks = []
        for task in tasks:
            if self.should_update(task, goal):
                evaluated_tasks.append(('update', task))
            elif self.should_delete(task, goal):
                evaluated_tasks.append(('delete', task))
        return evaluated_tasks

    def should_update(self, task: str, goal: str) -> bool:
        # Actual logic to determine if a task should be updated
        # Placeholder for demonstration purposes
        return 'update' in task

    def should_delete(self, task: str, goal: str) -> bool:
        # Actual logic to determine if a task should be deleted
        # Placeholder for demonstration purposes
        return 'delete' in task