import os

old_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="me-2"><path d="M4 7H20L18.5 21H5.5L4 7Z" fill="var(--color-primary)" fill-opacity="0.2" stroke="var(--color-primary)" stroke-width="2" stroke-linejoin="round"/><path d="M8 7L12 3L16 7" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="14" r="3" fill="var(--color-secondary)"/></svg>'
new_svg = '<svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg" class="me-2"><path d="M8.5 20.5H22.5L25 9.5H7.5L5.5 3H2" stroke="var(--color-primary)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="10.5" cy="24.5" r="2" fill="var(--color-secondary)"/><circle cx="20.5" cy="24.5" r="2" fill="var(--color-secondary)"/><path d="M12 12C12 9 15 6 18 6C18 9 15 12 12 12Z" fill="var(--color-secondary)"/><path d="M18 6C20 6 22 8 22 10C22 12.5 19 14.5 16 15" stroke="var(--color-secondary)" stroke-width="1.5" stroke-linecap="round"/></svg>'

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(old_svg, new_svg)
        content = content.replace('RubyBasket', 'DailyGrocery')
        content = content.replace('rubybasket.com', 'dailygrocery.com')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Logo and text replaced successfully.")
