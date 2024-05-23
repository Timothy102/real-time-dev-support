# Greptile - Real-Time Developer Support

Welcome to Greptile, a real-time developer support system powered by a combination of Large Language Models (LLM) and human assistance.

## Idea: Real-Time Developer Support (LLM + Person)

### Scope:

- For a developer building on top of some other company’s code to chat with an assistant and get answers to issues he cannot resolve, and/or to make code changes/tests/reviews.
- Later if the code still couldn’t have been resolved, for the internal support team to be created a ticket, and have the assistant point him at the relevant code and help the dev out.

### Product Workflow:

1. This product should be importable like [chatbase.com](http://chatbase.com) and be added as an assistant to a dev support website.
   - Client-facing SaaS (like chatbase.com) allows companies to connect their Github and select the appropriate repo — Tailwind frontend.
   - They can copy custom iframe & html scripts that are easily embedded onto websites as chatbots.
     - Need to spin out each chatbot on a different npm server. Currently just one is working for local testing purposes. I modified the [`chatbot-ui`](https://github.com/mckaywrigley/chatbot-ui) to POST on greptile.
   - They can then easily import these chatbots as iframe or through pure html into their websites.
   - A 3rd party developer interacts with the chatbot. If he has trouble resolving his issue, he can ask for support of the technical team. In which case, a Slack notification involving last `model_response`, `user_request`, and `support_ticket` are sent to a member of the technical team. That member can type his response back in the Slack channel and his response will appear on the developer’s chatbot. This is great because it brings the member of the technical member up to speed immediately and allows for zero friction transition from an LLM to a person.

## Conclusive Thoughts

### Improvements:

1. **Design**
    - Tailwind components all the way.
2. **Serving**
    - Eliminating 90% of the code that chatbot-ui holds for inferencing LLMs from OpenAI, Anthropic, Gemini, etc.
    - Actual chatbot-ui creation and hosting for each repo — embedded next.js runtimes/different microservices, let’s skip for now.
3. **Developer-support interactions**
    - We should spend time observing the requests and interactions from developer to build better retrieval models. I have not spent time here.

### Why I think it’s a great idea:

1. As a developer, I had always found time and effort-consuming to understand and dig my way through large codebases when implementing open-source workflows, particularly when dealing with:
    - Custom types
    - Error/exception handling
    - Module installation (circular dependencies 😠)
2. I believe it’s a big frustration among other developers as well and a solution like this would almost eliminate the friction to adopt new technologies and would skyrocket the efficacy of technical support teams which big enterprise is delighted to offer.
3. I believe it is and will continue to evolve into an ever bigger market and we should be the one to bring this to market.

---# greptile
