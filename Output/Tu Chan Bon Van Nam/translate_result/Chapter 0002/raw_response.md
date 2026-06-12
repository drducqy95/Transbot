I will list the contents of the root workspace directory `/mnt/sdcard/My Agent/Transbot` to understand the project structure and see how translations are organized.
I will list the contents of the `Source` directory to see the input chapters.
I will list the contents of the `Output` and `Script` directories to see where translations are saved and check for existing translation helper scripts or tools.
I will list the `Output` directory to understand how the outputs of different chapters are structured.
I will list the contents of the `Output/Tu Chan Bon Van Nam` directory to examine the existing translation outputs.
I will list `Output/Tu Chan Bon Van Nam/pre_trans` to see if there is any pre-processed file for chapter 2.
I will check the files inside `Output/Tu Chan Bon Van Nam/pre_trans/Chapter 0002` to see the structure of the source segments.
I will list the `Output/Tu Chan Bon Van Nam/output` directory to see if there is any output for Chapter 1 or 2.
I will list the `Output/Tu Chan Bon Van Nam/translate_result` directory.
I will list `Output/Tu Chan Bon Van Nam/translate_result/Chapter 0002` to see its contents.
I will list the contents of `Output/Tu Chan Bon Van Nam/pre_trans/Chapter 0001` and `Output/Tu Chan Bon Van Nam/translate_result/Chapter 0001` to check the structure of completed translations.
I will list the contents of `Output/Tu Chan Bon Van Nam/translate_result/Chapter 0001`.
I will view the beginning of `Output/Tu Chan Bon Van Nam/translate_result/Chapter 0001/translated_segments.json` to see the format of the output.
I will view the `Output/Tu Chan Bon Van Nam/pre_trans/Chapter 0002/source.md` file to see the source segments that need to be translated.
I will view `Output/Tu Chan Bon Van Nam/pre_trans/Chapter 0002/context_pack.md` to see any context instructions, glossary terms, or character mappings provided for this chapter.
I will view the contents of `Script/pipeline_tu-chan-bon-van-nam.py` to see the pipeline workflow and how the translation for a chapter is processed.
I will view lines 150 to 350 of the script `Script/pipeline_tu-chan-bon-van-nam.py` to see the logic for loading files, parsing segments, calling translation, and saving outputs.
I will view lines 351 to 594 of `Script/pipeline_tu-chan-bon-van-nam.py` to see the complete main function.
I will view the first 30 lines of `Output/Tu Chan Bon Van Nam/pre_trans/Chapter 0001/source.md` to see if it matches the segments of Chapter 1.
I will view the `glossary_scan.json` file for Chapter 2 to see the terms identified for normalization.
I will check `Output/Tu Chan Bon Van Nam/pre_trans/Chapter 0002/ai_review.json` to see the AI review and potential translations of the terms.