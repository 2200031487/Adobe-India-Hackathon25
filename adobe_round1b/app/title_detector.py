import re

def get_title_candidates(text):
    lines = text.split('\n')
    title_lines = []
    
    for line in lines:
        clean = line.strip()
        
        # Skip empty lines
        if not clean:
            continue
            
        # Look for title patterns
        # 1. Lines that are title case and not too long
        if (clean.istitle() and len(clean) > 3 and len(clean) < 80):
            title_lines.append(clean)
        
        # 2. Lines that are all caps (but not too long)
        elif (clean.isupper() and len(clean) > 3 and len(clean) < 50):
            title_lines.append(clean)
        
        # 3. Lines that start with common section indicators
        elif re.match(r'^(Chapter|Section|Part|Introduction|Conclusion)\s+', clean, re.IGNORECASE):
            title_lines.append(clean)
        
        # 4. Lines that end with colons (section headers)
        elif clean.endswith(':') and len(clean) > 5 and len(clean) < 60:
            title_lines.append(clean)
        
        # 5. Lines with specific formatting patterns
        elif re.match(r'^[A-Z][a-zA-Z\s-]+[A-Z].*$', clean) and len(clean) < 60:
            title_lines.append(clean)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_titles = []
    for title in title_lines:
        if title not in seen:
            seen.add(title)
            unique_titles.append(title)
    
    # Return top 3 title candidates
    return unique_titles[:3]