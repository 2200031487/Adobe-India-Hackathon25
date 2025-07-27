def rank_sections(sections, keywords):
    ranked = []
    for sec in sections:
        text = sec["text"].lower()
        lines = sec["raw_lines"]
        score = 0

        # Calculate keyword scores with different weights
        for kw in keywords:
            kw_lower = kw.lower()
            # Higher score for keywords in main text
            score += text.count(kw_lower) * 3
            
            # Additional score for keywords in individual lines
            for line in lines:
                if kw_lower in line.lower():
                    score += 1

        # Bonus for longer content (more likely to be substantial)
        if len(text) > 500:
            score += 2
        elif len(text) > 200:
            score += 1

        # Only include sections with some relevance
        if score > 0:
            ranked.append({
                "page": sec["page"],
                "text": sec["text"],
                "lines": lines,
                "importance_rank": score
            })

    # Sort by score in descending order
    ranked.sort(key=lambda x: -x["importance_rank"])
    return ranked