"""
NeoXBridge AI - LLM Client
Client for interacting with OpenAI API to power conversational AI.
"""

import os
import logging
import openai

logger = logging.getLogger(__name__)


class LLMClient:
    """Client for interacting with the OpenAI API."""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.client = None
        self.logger = logging.getLogger(__name__ + ".LLMClient")
    
    async def initialize(self):
        """Initialize the OpenAI client."""
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        
        try:
            self.client = openai.AsyncOpenAI(api_key=self.api_key)
            self.logger.info(f"LLM client initialized with model: {self.model}")
        except Exception as e:
            self.logger.error(f"Failed to initialize OpenAI client: {e}")
            raise
    
    async def generate_response(
        self, 
        prompt: str, 
        max_tokens: int = 150, 
        temperature: float = 0.5
    ) -> str:
        """
        Generate a response from the LLM.
        
        Args:
            prompt (str): The prompt to send to the LLM
            max_tokens (int): Maximum number of tokens to generate
            temperature (float): Controls randomness (0.0 to 1.0)
            
        Returns:
            str: The generated response text
        """
        if not self.client:
            raise ConnectionError("LLM client not initialized. Call initialize() first.")
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
                n=1,
                stop=None,
            )
            
            if response.choices:
                return response.choices[0].message.content.strip()
            
            return "I'm sorry, but I couldn't generate a response. Please try again."
            
        except openai.APIError as e:
            self.logger.error(f"OpenAI API error: {e}")
            return "I am experiencing issues with my AI provider. Please try again later."
        except Exception as e:
            self.logger.error(f"Error generating LLM response: {e}")
            return "I encountered an unexpected error while generating a response."
    
    async def get_available_models(self) -> list[str]:
        """
        Get a list of available models from OpenAI.
        
        Returns:
            list[str]: A list of available model names
        """
        if not self.client:
            raise ConnectionError("LLM client not initialized. Call initialize() first.")
        
        try:
            models = await self.client.models.list()
            return [model.id for model in models.data]
        except Exception as e:
            self.logger.error(f"Failed to retrieve models: {e}")
            return []
