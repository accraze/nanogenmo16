from internetarchive import download

ia_corpus_names = [
    'flatlandromanceo00abbouoft',
    'YouDontNeedAWeathermanToKnowWhichWayTheWindBlows_925',
    'FuturistManifesto',
    'TheSilverPanthersOfLunaAVisualCompanion',
    'btthg31.pdf',
    'al_FC_Industrial_Society_and_Its_Future_a4'
]

for name in ia_corpus_names:
    download(name, verbose=True, glob_pattern="*.txt")
