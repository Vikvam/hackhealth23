from phir import get_extension_value


class DG:
    def __init__(self, id, chromosome, region, type, reference, allele, length, count, coverage, frequency,
                 forward_reverse_balance, average_quality, gene_name, coding_region_change, amino_acid_change,
                 exon_number, type_of_mutation):
        self.id = id
        self.chromosome = chromosome
        self.region = region
        self.type = type
        self.reference = reference
        self.allele = allele
        self.length = length
        self.count = count
        self.coverage = coverage
        self.frequency = frequency
        self.forward_reverse_balance = forward_reverse_balance
        self.average_quality = average_quality
        self.gene_name = gene_name
        self.coding_region_change = coding_region_change
        self.amino_acid_change = amino_acid_change
        self.exon_number = exon_number
        self.type_of_mutation = type_of_mutation

    @staticmethod
    def from_fhir(fhir: dict):
        fhir = fhir["resource"]
        id = fhir["id"]
        dg = DG(
            id,
            get_extension_value(fhir, "chromosome"),
            get_extension_value(fhir, "region"),
            get_extension_value(fhir, "type"),
            get_extension_value(fhir, "reference"),
            get_extension_value(fhir, "allele"),
            get_extension_value(fhir, "length"),
            get_extension_value(fhir, "count"),
            get_extension_value(fhir, "coverage"),
            get_extension_value(fhir, "frequency"),
            get_extension_value(fhir, "Forward/Reverse Balance"),
            get_extension_value(fhir, "Average quality"),
            get_extension_value(fhir, "Gene name"),
            get_extension_value(fhir, "Coding Region Change"),
            get_extension_value(fhir, "Amino Acid Change"),
            get_extension_value(fhir, "Exon Number"),
            get_extension_value(fhir, "Type of mutation")
        )
        return dg

    def as_json(self):
        return {
            "id": self.id,
            "Chromosome": self.chromosome,
            "Region": self.region,
            "Type": self.type,
            "Reference": self.reference,
            "Allele": self.allele,
            "Length": self.length,
            "Count": self.count,
            "Coverage": self.coverage,
            "Frequency": self.frequency,
            "Forward Reverse Balance": self.forward_reverse_balance,
            "Average Quality": self.average_quality,
            "Gene Name": self.gene_name,
            "Coding Region Change": self.coding_region_change,
            "Amino Acid Change": self.amino_acid_change,
            "Exon Number": self.exon_number,
            "Type of Mutation": self.type_of_mutation
        }
