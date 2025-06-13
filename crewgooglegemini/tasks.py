from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

research_task=Task(
    description=(
        "Identify the new big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points."
        "its market oppurtunities, and potential risks"
    ),
    expected_output='A comprehensive 2 paragraphs long report on the {topic}',
    tools=[tool],
    agent = [news_researcher]
)

# Creating a writer agent with custom tools responsible for writing news blog
write_task=Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to undersand, engaging, and positive."
    ),
    expected_output='A 3 paragraph article on {topic} advancements formatted as markdown.',
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file='new-blog-post.txt' #example of output customization
)