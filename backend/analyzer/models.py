from django.db import models

# Defines the database model for storing the results of a domain analysis.
class AnalysisResult(models.Model):
    """
    Represents a single analysis result stored in the database.
    Each instance holds the generated insights for a specific domain.
    """

    # The domain that was analyzed (e.g., "healthcare", "fintech").
    domain = models.CharField(max_length=255)

    # The timestamp when this analysis was created.
    # `auto_now_add=True` automatically sets this to the current time on creation.
    created_at = models.DateTimeField(auto_now_add=True)

    # The list of generated startup ideas, stored as a JSON object.
    # JSONField is ideal for structured but flexible data like a list of dicts.
    startup_list = models.JSONField()

    # The detailed text analysis of market trends.
    # TextField is used for large blocks of text.
    trends_analysis = models.TextField()

    # The summary of investment potential and strategy.
    investment_summary = models.TextField()

    def __str__(self):
        """
        Returns a human-readable string representation of the model instance.
        This is used in the Django admin interface and for debugging.
        """
        
        return f"Analysis on {self.domain} ({self.created_at})"
