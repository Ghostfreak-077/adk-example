import os

try:
    from dotenv import load_dotenv
    load_dotenv()

    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL","gemini-2.0-flash")
except ImportError:
    print("Warning: python-dotenv is not installed. Ensure API key is set")
    MODEL_NAME = "gemini-2.0-flash"

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

from multi_tool_agent.instructions import MARKET_RESEARCH_INSTRUCTION, CAMPAIGN_ORCHESTRATOR_INSTRUCTION

market_research_tool = LlmAgent(
    name="MarketResearcher",
    instruction=MARKET_RESEARCH_INSTRUCTION,
    model=MODEL_NAME,
    tools=[google_search],
    output_key="market_research_summary"
)

campaign_orchestration_agent = SequentialAgent(
    name="CAMPAIGN_ORCHESTRATOR",
    sub_agents=[market_research_tool],
    description=CAMPAIGN_ORCHESTRATOR_INSTRUCTION
)

root_agent = campaign_orchestration_agent