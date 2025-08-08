from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List
from ventureviz.tools.enrich_company_tool import EnrichCompanyTool

@CrewBase
class Ventureviz():
    """Ventureviz crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def startup_scout(self) -> Agent:
        """
            Creates the startup scout agent

            This agent is responsible for researching and identifying startups in a particular domain.
            Returns:
                    Agent:- A CrewAI agent configured for startup scouting.
        """

        return Agent(
            config=self.agents_config['startup_scout'],
            tools=[SerperDevTool()],
            max_iter=3, # Limit the number of times the tool is executed by the Agent
            memory=True,
            verbose=True
        )
    
    @agent
    def company_enricher(self) -> Agent:
        """
            Creates the company enricher agent

            This agent is responsible for enriching startup leads with metadata to make downstream VC evaluation more insightful.
            Returns:
                    Agent:- A CrewAI agent configured for company enrichment.
        """

        return Agent(
            config=self.agents_config['company_enricher'],
            tools=[EnrichCompanyTool()],
            memory=True,
            verbose=True
        )

    @agent
    def trend_analyst(self) -> Agent:
        """
            Creates the trend analyst agent

            This agent is responsible for uncovering trends and patterns among startups in a given domain.
            Returns:
                    Agent:- A CrewAI agent configured for trend analysis.
        """

        return Agent(
            config=self.agents_config['trend_analyst'],
            memory=True,
            verbose=True
        )
    
    @agent
    def vc_advisor(self) -> Agent:
        """
            Creates the VC advisor agent

            This agent is responsible for generating investment recommendations based on startup findings and trend analysis.
            Returns:
                    Agent:- A CrewAI agent configured for VC recommendations.
        """

        return Agent(
            config=self.agents_config['vc_advisor'],
            memory=True,
            verbose=True
        )

    @task
    def scout_startups(self) -> Task:
        """
            Creates the scout startups task

            This task defines the workflow for researching and identifying startups in a particular domain.
            The @task decorator marks this method as a task factory for the CrewAI framework.
            Returns:
                    Task:- A CrewAI task configured for startup scouting.
        """

        return Task(
            config=self.tasks_config['scout_startups'],
        )

    @task
    def enrich_startups(self) -> Task:
        """
            Creates the enrich startups task

            This task defines the workflow for enriching startup companies discovered in the previous task using a custom tool.
            Returns:
                    Task:- A CrewAI task configured for company enrichment.
        """

        return Task(
            config=self.tasks_config['enrich_startups'],
        )

    @task
    def analyze_trends(self) -> Task:
        """
            Creates the analyze trends task

            This task defines the workflow for uncovering trends and patterns among startups in a given domain.
            Returns:
                    Task:- A CrewAI task configured for trend analysis.
        """

        return Task(
            config=self.tasks_config['analyze_trends'],
        )

    @task
    def investment_recommendation(self) -> Task:
        """
            Creates the investment recommendation task

            This task defines the workflow for generating investment recommendations based on startup findings and trend analysis.
            Returns:
                    Task:- A CrewAI task configured for VC recommendations.
        """

        return Task(
            config=self.tasks_config['investment_recommendation'],
        )
    
    @crew
    def crew(self) -> Crew:
        """
            Creates and configures the Backend crew.
            
            This method assembles the complete crew by combining the curriculum designer
            and content curator agents with their respective tasks. The crew processes
            tasks sequentially to ensure proper workflow execution. The @crew decorator
            marks this method as the main crew factory for the CrewAI framework.
            
            Returns:
                Crew: A configured CrewAI Crew with agents, tasks, and sequential processing
        """

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            max_rpm=8,
            verbose=True
        )