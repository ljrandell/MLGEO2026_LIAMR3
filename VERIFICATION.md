| Verifier | Tool and model | Ran the code? | Read the repo correctly? | Environment and compute | Code and workflow | Data and provenance | Publication and credit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Human: Myself | none | yes | yes | 2 | 1 | N/A | 1 |
| Agent | Copilot: VSCode | yes | yes | 2 | 1 | 1 | 1 |
| Chatbot | Purple, GPT-5.6 Luna | no | no | N/A | N/A | N/A | N/A |
| Chatbot | Purple, Claude Sonnet 5 | yes (with help via uploaded file) | yes | 2 | 1 | N/A | 0 |

The main point of disagreement came with _Data and Provenance_ and _Publication and credit_, wherein only the VSCode Copilot gave a non N/A rating for _Data and Provenance_ and only Claude Sonnet 5 gave a 0 for _Publication and credit_. These two catergories are the most difficult to grade, with _Data and Provenance_ relying on grading a repo without any distinct data as of present, and _Publication and credit_ additionally difficult as I have not ironed it out fully. The VSCode Copilot was the only bot to fully run and read the repo without needing help with uploaded files, while GPT-5.6 Luna failed just about entirely. One thing that stood out among the recommendations was the importance of having additional files to test, so I added additional instructions to run the added `.py` and `.ipynb` files as further verification.