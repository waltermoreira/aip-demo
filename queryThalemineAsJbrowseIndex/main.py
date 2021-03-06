
MAPPING = {
    'Gene': 'TAIR10_loci',
    'Pseudogene': 'TAIR10_pseudogenes',
    'TransposableElement': 'TAIR10_transposons',
    'TransposableElementGene': 'TAIR10_transposons',
    'MRNA': 'TAIR10_gene_models',
    'miRNA': 'TAIR10_ncrnas',
    'rRNA': 'TAIR10_ncrnas',
    'snRNA': 'TAIR10_ncrnas',
    'snoRNA': 'TAIR10_ncrnas',
    'tRNA': 'TAIR10_ncrnas'
}

def map_filter(arg):
    new_tracks = list(filter(None, map(MAPPING.get, arg['location']['tracks'])))
    if new_tracks:
        arg['location']['tracks'] = new_tracks
        return arg
