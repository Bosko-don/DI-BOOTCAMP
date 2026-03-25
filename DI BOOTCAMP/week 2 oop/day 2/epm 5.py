#!/usr/bin/env python3
"""
BIOLOGY DNA CHALLENGE
Topics: OOP, Inheritance, Polymorphism
"""

import random


class Gene:
    """A single gene with value 0 or 1 that can mutate (flip)"""
    
    def __init__(self, value=None):
        if value is None:
            self.value = random.choice([0, 1])
        else:
            self.value = value
    
    def mutate(self):
        """Flip the gene value (0 becomes 1, 1 becomes 0)"""
        self.value = 1 - self.value  # Simple flip: 0→1, 1→0
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"Gene({self.value})"


class Chromosome:
    """A series of 10 Genes that can mutate"""
    
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]
    
    def mutate(self):
        """Random number of genes randomly flip (50% chance each)"""
        for gene in self.genes:
            if random.random() < 0.5:  # 50% chance to flip each gene
                gene.mutate()
    
    def is_all_ones(self):
        """Check if all genes in this chromosome are 1"""
        return all(gene.value == 1 for gene in self.genes)
    
    def __str__(self):
        return "".join(str(gene) for gene in self.genes)
    
    def __repr__(self):
        return f"Chromosome({self.__str__()})"


class DNA:
    """A series of 10 Chromosomes that can mutate"""
    
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]
    
    def mutate(self):
        """Random number of chromosomes randomly mutate (50% chance each)"""
        for chromosome in self.chromosomes:
            if random.random() < 0.5:  # 50% chance each chromosome mutates
                chromosome.mutate()
    
    def is_all_ones(self):
        """Check if all genes in all chromosomes are 1 (perfect DNA)"""
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)
    
    def get_gene_count(self):
        """Count total 1s across all chromosomes"""
        return sum(
            sum(gene.value for gene in chromosome.genes)
            for chromosome in self.chromosomes
        )
    
    def __str__(self):
        return "\n".join(f"Chr{i}: {chromosome}" for i, chromosome in enumerate(self.chromosomes))
    
    def __repr__(self):
        return f"DNA({len(self.chromosomes)} chromosomes)"


class Organism:
    """An organism with DNA that mutates based on environment probability"""
    
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment  # Probability of mutation (0.0 to 1.0)
        self.generations = 0
    
    def attempt_mutation(self):
        """Try to mutate based on environment probability"""
        if random.random() < self.environment:
            self.dna.mutate()
            self.generations += 1
            return True
        return False
    
    def is_perfect(self):
        """Check if organism has achieved perfect DNA (all 1s)"""
        return self.dna.is_all_ones()
    
    def __str__(self):
        return f"Organism(gen={self.generations}, env={self.environment}, perfect={self.is_perfect()})"


def run_evolution_simulation(num_organisms=5, environment=0.3, max_generations=10000):
    """
    Run evolution simulation until one organism achieves perfect DNA
    """
    print("=" * 60)
    print("🧬 BIOLOGY EVOLUTION SIMULATION 🧬")
    print("=" * 60)
    print(f"\nParameters:")
    print(f"  - Number of organisms: {num_organisms}")
    print(f"  - Environment (mutation probability): {environment}")
    print(f"  - Max generations: {max_generations}")
    print(f"\nGoal: Achieve DNA with all 1s (100 genes total)")
    
    # Create initial organisms
    organisms = [Organism(DNA(), environment) for _ in range(num_organisms)]
    
    print(f"\n--- Initial State ---")
    for i, org in enumerate(organisms):
        ones = org.dna.get_gene_count()
        print(f"Organism {i}: {ones}/100 ones")
    
    # Evolution loop
    generation = 0
    winner = None
    
    while generation < max_generations and winner is None:
        generation += 1
        
        for i, organism in enumerate(organisms):
            organism.attempt_mutation()
            
            if organism.is_perfect():
                winner = i
                print(f"\n{'='*60}")
                print(f"🎉 WINNER FOUND! 🎉")
                print(f"{'='*60}")
                print(f"Organism {winner} achieved perfect DNA!")
                print(f"Total generations: {organism.generations}")
                print(f"Final DNA:")
                print(organism.dna)
                break
        
        # Progress update every 1000 generations
        if generation % 1000 == 0:
            best = max(organisms, key=lambda o: o.dna.get_gene_count())
            print(f"Gen {generation}: Best organism has {best.dna.get_gene_count()}/100 ones")
    
    if winner is None:
        print(f"\n⚠️ No winner after {max_generations} generations")
        best = max(organisms, key=lambda o: o.dna.get_gene_count())
        print(f"Best organism achieved: {best.dna.get_gene_count()}/100 ones")
    
    return winner, generation


def research_notebook():
    """
    Run multiple experiments and record results
    """
    print("\n" + "=" * 60)
    print("📓 RESEARCH NOTEBOOK - Multiple Experiments")
    print("=" * 60)
    
    experiments = [
        {"organisms": 3, "environment": 0.1},
        {"organisms": 5, "environment": 0.3},
        {"organisms": 10, "environment": 0.5},
        {"organisms": 5, "environment": 0.8},
        {"organisms": 20, "environment": 0.5},
    ]
    
    results = []
    
    for exp in experiments:
        print(f"\n{'='*40}")
        print(f"Experiment: {exp['organisms']} organisms, env={exp['environment']}")
        
        winner, generations = run_evolution_simulation(
            num_organisms=exp['organisms'],
            environment=exp['environment'],
            max_generations=5000
        )
        
        results.append({
            "organisms": exp['organisms'],
            "environment": exp['environment'],
            "generations": generations if winner is not None else "Failed",
            "success": winner is not None
        })
    
    # Print conclusions
    print("\n" + "=" * 60)
    print("🔬 CONCLUSIONS")
    print("=" * 60)
    
    for r in results:
        status = "✅ Success" if r['success'] else "❌ Failed"
        print(f"Org: {r['organisms']:2d} | Env: {r['environment']:.1f} | Gen: {r['generations']:<6} | {status}")
    
    print(f"\n📊 Key Findings:")
    print(f"1. Higher environment (mutation rate) = faster evolution")
    print(f"2. More organisms = higher chance of success")
    print(f"3. Balance needed: too high mutation = chaos, too low = stagnation")
    print(f"4. Randomness plays significant role in evolution!")


if __name__ == "__main__":
    # Run single simulation
    run_evolution_simulation(num_organisms=5, environment=0.3)
    
    # Run research notebook with multiple experiments
    print("\n" + "=" * 60)
    response = input("Run full research notebook? (y/n): ").strip().lower()
    if response == 'y':
        research_notebook()