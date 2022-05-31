from Bio import SeqIO

def make_gene_list(gene_id, dir, gene_name="unknown_gene"):
    gene_list = []  
    for file in os.listdir(dir):  
        f = os.path.join(dir, file)
        if os.path.isfile(f):
            sample_name = file.split("_")[0]
            for record in SeqIO.parse(f, "fasta"):
                if record.id == gene_id:
                    new_record = SeqIO.SeqRecord(record.seq, sample_name, "", "")
                    gene_list.append(new_record)
    SeqIO.write(gene_list, "consensus_"+gene_name+".fasta", "fasta")
                    
make_gene_list("NC_005783.5:102437-104626","./consensus",gene_name="AgWHI3")