from Bio import SeqIO

records = list(SeqIO.parse("ashbya_cds.fna", "fasta"))

# Make regions list for all CDS
# gene_list.tsv was used in Snakefile on Longleaf 
gene_list = []
with open('gene_list.tsv', 'w') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    for record in records:
        chrom = record.description.split()[0][4:15]
        loc = record.description.split()[5]
        if "join" in loc:
            pass
        elif "complement" in loc:
            loc = loc.split("(")[1].split(".")
            loc2 = loc[2][:-2]
            loc1 = loc[0]
            tsv_writer.writerow([chrom+":"+loc1+"-"+loc2])
        else:
            loc = test.split("=")[1].split(".")
            loc2 = loc[2][:-1]
            loc1 = loc[0]
            tsv_writer.writerow([chrom+":"+loc1+"-"+loc2])




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
