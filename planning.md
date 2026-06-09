# AI201 First Project – FPGA Radiation RAG


## Domain

Unofficial Guide to FPGA Radiation Testing, Radiation Effects, Radiation Detection, and Radiation-Tolerant FPGA Design

This system helps students, engineers, and researchers understand FPGA radiation effects, mitigation techniques, and radiation-testing practices. Information on this topic is difficult to find because it is scattered across NASA reports, FPGA vendor documentation, academic papers, and technical presentations.

The system will make this knowledge searchable through a retrieval-augmented question-answering interface. The knowledge base covers radiation-induced faults in FPGAs, mitigation techniques such as TMR and SEM, fault-injection methodologies, radiation-testing procedures, and radiation-sensing materials research.




## Source Documents
1. NASA FPGA Single Event Effect Radiation Test Guidelines
   URL: https://nepp.nasa.gov/files/23779/FPGA_Radiation_Test_Guidelines_2012.pdf

2. NASA/JPL Assessing and Mitigating Radiation Effects in Xilinx FPGAs
   URL: https://nepp.nasa.gov/DocUploads/08A3733D-6D42-428C-824E76B5B5A92B59/07-113%20Adell_JPL%20Assessing%20and%20Mitigating%20Rad%20effects.pdf

3. NASA Electronic Parts and Packaging FPGA SEE Test Guideline Update (Presentation)
   URL: https://ntrs.nasa.gov/api/citations/20180001945/downloads/20180001945.pdf

4. AMD/Xilinx LogiCORE IP Soft Error Mitigation Controller User Guide (UG764)
   URL: https://docs.amd.com/v/u/1.0-English/sem_ug764

5. Single Event Effects in FPGA Devices: Update 2020
   URL: https://ntrs.nasa.gov/api/citations/20205003879/downloads/2020-561-Berg-Final-Presentation-NEPP-ETW_v3.pdf

6. NASA NEPP FPGA Tasks and Considerations
   URL: https://ntrs.nasa.gov/api/citations/20140017354/downloads/20140017354.pdf

7. Using Classical Reliability Models and Single Event Upset (SEU) Data to Determine Optimum Implementation Schemes for Triple Modular Redundancy (TMR) in SRAM-Based Field Programmable Gate Array (FPGA) Devices
   URL: https://ntrs.nasa.gov/api/citations/20150018112/downloads/20150018112.pdf

8. Single Event Analysis and Fault Injection Techniques Targeting Complex Designs Implemented in Xilinx-Virtex FPGA Devices
   URL: https://ntrs.nasa.gov/api/citations/20140008976/downloads/20140008976.pdf

9. Modernizing Single Event Effect Test and Analysis Methods for Complex FPGA Applications
   URL: https://ntrs.nasa.gov/api/citations/20230005923/downloads/Berg_HEART_2023_v2a.pdf

10. Noise Impact of Single Event Upsets on an FPGA-Based Digital Filter
    URL: https://www.nsf-shrec.org/sites/default/files/2024-03/Noise-impact-of-single-event-upsets-on-an-fpga-based-digital-filter.pdf

11.   X-ray Radiation Effects on SWCNT/PMMA Thin Film Nanocomposites
      Authors: Suman, G., Pulikkathara, M., & Wilkins, R.
      Source: IEEE Transactions on Nanotechnology, Vol. 20, pp. 517–524, 2021.
      DOI: 10.1109/TNANO.2021.3080624

12. Ionizing Radiation Sensing with Functionalized and Copper-Coated SWCNT/PMMA Thin Film Nanocomposites.
    Authors: Suman, G., Pulikkathara, M., Wilkins, R., & Treadwell, L. J.
    Source: Nanomaterials, Vol. 13, Article 2653, 2023.
    DOI: 10.3390/nano13192653

13. X-ray Radiation Effects on Thin Film Nanocomposites of Functionalized and Copper-Coated Multi-Walled Carbon Nanotube and Poly(Methyl Methacrylate)
    Authors: Kyatsandra, S., Pulikkathara, M., & Wilkins, R. 
    Source: Surfaces and Interfaces, Vol. 17, Article 100362, 2019
     https://doi.org/10.1016/j.surfin.2019.100362




## Example Questions the System Should Answer


1. What is a Single Event Upset (SEU) in an FPGA?

2. Why are SRAM-based FPGAs vulnerable to radiation?

3. What is Triple Modular Redundancy (TMR) and how does it improve reliability?

4. What is the function of the Xilinx Soft Error Mitigation (SEM) core?

5. What measurements should be collected during an FPGA radiation test?

6. What is the difference between a configuration upset and a data upset?

7. How are fault injection experiments used to study FPGA radiation effects?

8. What are the tradeoffs between TMR and DMR mitigation techniques?
   
9. How do carbon nanotube nanocomposites respond to X-ray radiation?

10. What properties make SWCNT/PMMA nanocomposites suitable for radiation sensing?


## Chunking Strategy

I will use fixed-size chunks of approximately 800 characters with an overlap of 150 characters.

My document collection consists primarily of NASA radiation-test guidelines, AMD/Xilinx FPGA documentation, fault-injection reports, and academic research papers. These documents contain technical explanations that often span multiple paragraphs and include concepts such as Single Event Upsets (SEUs), Triple Modular Redundancy (TMR), fault injection, radiation testing procedures, and radiation-sensing materials.

An 800-character chunk is large enough to preserve technical context while remaining small enough for precise semantic retrieval. A 150-character overlap helps ensure that important information is not lost when concepts cross chunk boundaries. For example, a discussion of TMR reliability, SEM operation, or FPGA fault injection may begin near the end of one chunk and continue into the next.

If chunks are too small, important technical explanations may be fragmented and retrieved incompletely. If chunks are too large, retrieval may return broad sections of documents containing unrelated information, reducing answer precision.

The overlap improves retrieval quality by ensuring that information located near chunk boundaries remains available in multiple chunks, increasing the likelihood that complete technical concepts can be retrieved.



## Retrieval Approach

I will use the sentence-transformers embedding model **all-MiniLM-L6-v2** together with **ChromaDB** as the vector database for semantic retrieval.

Each document chunk will be stored along with its associated metadata, including the source document name and chunk identifier. This metadata will enable retrieved information to be traced back to its original source and support source attribution during answer generation.

For each user query, the system will retrieve the **top five most relevant chunks (top-k = 5)**. Retrieving too few chunks may exclude important supporting information, while retrieving too many may introduce irrelevant content that can reduce the quality and accuracy of generated responses.

The use of semantic search allows retrieval based on meaning rather than exact keyword matching. For example, a query about *radiation-induced bit flips* may successfully retrieve documents discussing *Single Event Upsets (SEUs)* even when the exact query terms are not present in the text.

If this system were deployed in a production environment, I would investigate larger embedding models that provide stronger retrieval accuracy, improved understanding of technical and scientific terminology, and better support for longer contexts. However, these benefits would need to be balanced against increased computational requirements, memory usage, and response latency.





## Evaluation Plan

Question 1
Question: What is a Single Event Upset (SEU) in an FPGA?
Expected Answer:
An SEU is a radiation-induced change of state in a memory element, register, or configuration bit caused by a charged particle strike.
Question 2
Question: What is Triple Modular Redundancy (TMR)?
Expected Answer:
TMR uses three identical copies of a circuit and a voting mechanism to mask errors caused by radiation-induced faults.
Question 3
Question: What is the purpose of the Xilinx Soft Error Mitigation (SEM) Controller?
Expected Answer:
The SEM Controller detects, reports, and corrects configuration-memory upsets in Xilinx FPGAs.
Question 4
Question: Why are SRAM-based FPGAs vulnerable to radiation?
Expected Answer:
Their configuration information is stored in SRAM cells that can be altered by radiation-induced particle strikes, causing soft errors and configuration upsets.
Question 5
Question: How are fault-injection experiments used in FPGA radiation studies?
Expected Answer:
Fault injection deliberately introduces errors into FPGA designs to evaluate reliability, identify vulnerabilities, and assess mitigation techniques without requiring actual radiation exposure.




## Anticipated Challenges

1.	Technical information may span multiple paragraphs, causing important concepts to be split across chunk boundaries. Although overlap helps, some context may still be fragmented.
2.	Different documents may use different terminology for the same concept. For example, "Single Event Upset (SEU)," "soft error," and "configuration upset" may refer to related radiation-induced faults, which could affect retrieval quality.
3.	Retrieval may return chunks from radiation-sensing nanocomposite papers when the user intends to ask about FPGA mitigation techniques, since both document groups contain radiation-related terminology.
4.	Long NASA reports and FPGA user guides may contain tables, figures, equations, and references that do not convert cleanly into text during document ingestion.
5.	Grounding failures may occur if the language model attempts to answer using its general knowledge rather than the retrieved FPGA-radiation documents. Prompt design and source attribution will be used to reduce this risk.



## AI Tool Plan

I will use Claude as my primary AI coding assistant throughout the project. I will provide specific sections of this planning document and implementation requirements rather than asking Claude to design the system for me.
Document Ingestion
Input to Claude:
•	Domain description
•	Source document requirements
Task:
•	Implement PDF loading and text extraction functions for NASA reports, AMD/Xilinx documentation, and academic papers.
Expected Output:
•	Python functions for document ingestion and preprocessing.
Chunking
Input to Claude:
•	Chunking Strategy section from this planning document.
Task:
•	Implement chunking logic using 800-character chunks with 150-character overlap.
Expected Output:
•	A chunking function that produces overlapping chunks suitable for embedding.
Embedding and Vector Storage
Input to Claude:
•	Retrieval Approach section.
Task:
•	Generate embeddings using all-MiniLM-L6-v2 and store them in ChromaDB.
Expected Output:
•	Code for embedding generation and vector database storage.
Retrieval
Input to Claude:
•	Retrieval Approach section.
Task:

•	Implement semantic search that retrieves the top 5 most relevant chunks for a user query.
Expected Output:
•	Retrieval function returning ranked chunks and metadata.
Grounded Response Generation
Input to Claude:
•	Evaluation Plan
•	Grounding requirements
Task:
•	Implement response generation that answers questions using only retrieved FPGA-radiation documents and includes source attribution.
Expected Output:
•	Prompt construction and generation code that prevents the model from relying on outside knowledge.
Debugging and Refinement
Input to Claude:
•	Error messages
•	Retrieval results
•	Evaluation outcomes
Task:
•	Help diagnose chunking issues, retrieval failures, and grounding problems.
Expected Output:
•	Debugging suggestions and revised code while preserving the original design decisions.



## Architecture

FPGA Radiation Documents
(NASA Reports, AMD/Xilinx Manuals, Research Papers)
        │
        ▼
Document Ingestion (PDF Extraction)
        │
        ▼
Chunking (800 chars, 150 overlap)
        │
        ▼
Embeddings (all-MiniLM-L6-v2)
        │
        ▼
Vector Store (ChromaDB)
        │
        ▼
Retrieval (Top-5 Search)
        │
        ▼
Grounded Generation (Groq Llama 3.3 70B)
        │
        ▼
User Answer + Source Attribution