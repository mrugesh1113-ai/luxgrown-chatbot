from fpdf import FPDF
import os

def create_sample_catalog():
    pdf = FPDF()
    pdf.set_margins(15, 15, 15)
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 20)
    pdf.cell(0, 15, 'LUX GROWN', ln=True, align='C')
    pdf.set_font('Helvetica', 'I', 12)
    pdf.cell(0, 10, 'Premium Lab-Grown Diamond Jewelry', ln=True, align='C')
    pdf.ln(8)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 10, 'About Lux Grown', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(180, 7, 'Lux Grown is a premium lab-grown diamond jewelry brand based in Florida. We specialize in ethically sourced diamonds that are identical to mined diamonds. All diamonds are IGI or GIA certified. Every piece comes with a 30-day return policy and lifetime warranty.')
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 10, 'Why Choose Lab-Grown Diamonds?', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(180, 7, '40 to 60 percent less expensive than mined diamonds.')
    pdf.multi_cell(180, 7, 'Zero mining impact and no conflict sourcing.')
    pdf.multi_cell(180, 7, 'Identical chemical composition as mined diamonds.')
    pdf.multi_cell(180, 7, 'Same hardness, brilliance, and fire as mined diamonds.')
    pdf.multi_cell(180, 7, 'Every diamond comes with full IGI or GIA certification.')
    pdf.ln(4)

    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 12, 'Engagement Ring Collection', ln=True)
    pdf.ln(3)

    rings = [
        ('Classic Solitaire', '14K or 18K White Gold, Yellow Gold, or Rose Gold', '0.5ct to 3.0ct round brilliant', 'Starting at 899 dollars'),
        ('Halo Ring', '18K White Gold or Rose Gold', '0.75ct to 2.5ct center with pave halo', 'Starting at 1299 dollars'),
        ('Three-Stone Ring', '14K or 18K White Gold or Yellow Gold', '1.0ct to 4.0ct total carat weight', 'Starting at 1499 dollars'),
        ('Cushion Cut Solitaire', '14K Rose Gold or White Gold', '0.75ct to 2.0ct cushion cut', 'Starting at 1099 dollars'),
        ('Emerald Cut', 'Platinum or 18K White Gold', '0.5ct to 2.0ct emerald cut', 'Starting at 1199 dollars'),
        ('Oval Solitaire', '14K or 18K all metal types', '0.75ct to 2.5ct oval brilliant', 'Starting at 999 dollars'),
    ]
    for name, metal, stone, price in rings:
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, name, ln=True)
        pdf.set_font('Helvetica', '', 10)
        pdf.cell(0, 6, 'Metal: ' + metal, ln=True)
        pdf.cell(0, 6, 'Diamond: ' + stone, ln=True)
        pdf.cell(0, 6, 'Price: ' + price, ln=True)
        pdf.ln(3)

    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 12, 'Fine Jewelry', ln=True)
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 9, 'Necklaces', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, 'Solitaire Pendant: 0.25ct to 1.0ct on 18-inch chain. Starting at 399 dollars.', ln=True)
    pdf.cell(0, 6, 'Tennis Necklace: 2.0ct to 5.0ct total weight. Starting at 1899 dollars.', ln=True)
    pdf.cell(0, 6, 'Bezel Set Pendant: 0.5ct round or oval. Starting at 599 dollars.', ln=True)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 9, 'Earrings', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, 'Classic Studs: 0.25ct to 2.0ct total weight. Starting at 299 dollars.', ln=True)
    pdf.cell(0, 6, 'Diamond Hoops: 0.50ct to 1.5ct pave set. Starting at 699 dollars.', ln=True)
    pdf.cell(0, 6, 'Drop Earrings: 0.75ct to 2.0ct various shapes. Starting at 899 dollars.', ln=True)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 9, 'Bracelets', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, 'Tennis Bracelet: 3.0ct to 8.0ct total weight. Starting at 1499 dollars.', ln=True)
    pdf.cell(0, 6, 'Bangle: 1.0ct pave set diamonds. Starting at 899 dollars.', ln=True)
    pdf.ln(4)

    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 12, 'Policies and Care', ln=True)
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 9, 'Our Policies', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, 'Returns: 30-day free returns on all unworn items with free return shipping.', ln=True)
    pdf.cell(0, 6, 'Warranty: Lifetime warranty against defects, includes free annual cleaning.', ln=True)
    pdf.cell(0, 6, 'Resizing: One free ring resizing within the first year of purchase.', ln=True)
    pdf.cell(0, 6, 'Certification: All diamonds 0.5ct and above come with IGI or GIA certification.', ln=True)
    pdf.cell(0, 6, 'Shipping: Free insured shipping on all US orders, ships in 5 to 7 business days.', ln=True)
    pdf.cell(0, 6, 'Financing: Zero percent APR for 12 months through Affirm on orders over 500 dollars.', ln=True)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 9, 'Diamond Guide - The 4Cs', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, 'Cut: Excellent and Very Good grades only. Cut affects brilliance the most.', ln=True)
    pdf.cell(0, 6, 'Color: D through J range. D to F is colorless, G to J is near-colorless.', ln=True)
    pdf.cell(0, 6, 'Clarity: VS1 to SI2. All diamonds are eye-clean.', ln=True)
    pdf.cell(0, 6, 'Carat: 0.25ct to 5.0ct available. Lab diamonds cost 40 to 60 percent less per carat.', ln=True)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 13)
    pdf.cell(0, 9, 'Jewelry Care Instructions', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, 'Clean monthly with mild dish soap and warm water using a soft toothbrush.', ln=True)
    pdf.cell(0, 6, 'Remove jewelry before swimming, showering, or applying lotions and perfumes.', ln=True)
    pdf.cell(0, 6, 'Store pieces separately in a soft pouch to prevent scratching.', ln=True)
    pdf.cell(0, 6, 'Avoid chlorine and harsh chemicals as they can damage gold alloys.', ln=True)
    pdf.cell(0, 6, 'Bring in for professional cleaning once a year, free with your warranty.', ln=True)
    pdf.cell(0, 6, 'Prong settings should be checked annually to ensure diamond security.', ln=True)

    os.makedirs('docs', exist_ok=True)
    output_path = os.path.join('docs', 'luxgrown_product_catalog.pdf')
    pdf.output(output_path)
    print('Sample catalog created at: ' + output_path)
    print('Now run: python ingest.py')

if __name__ == '__main__':
    create_sample_catalog()
