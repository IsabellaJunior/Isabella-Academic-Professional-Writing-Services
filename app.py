import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Isabella - Premium Writing Services", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    h1, h2, h3 { color: #1e293b !important; }
    .stButton > button { background-color: #059669; color: white; border: none; border-radius: 8px; padding: 0.6rem 2rem; font-weight: 600; }
    .stButton > button:hover { background-color: #047857; transform: translateY(-2px); }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: white; padding: 8px 12px; border-radius: 12px; border-bottom: 2px solid #e2e8f0; flex-wrap: wrap; }
    .stTabs [data-baseweb="tab"] { padding: 6px 14px; border-radius: 8px; font-weight: 500; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #3b82f6; color: white; }
    .trust-badge { background-color: #f1f5f9; padding: 1rem; border-radius: 12px; text-align: center; margin: 1.5rem 0; }
    .testimonial-card { background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #e2e8f0; height: 100%; }
    .testimonial-card .stars { color: #f59e0b; }
    .testimonial-card p { font-style: italic; }
    .payment-details { background-color: #f1f5f9; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #059669; }
    .pricing-card { background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #e2e8f0; text-align: center; height: 100%; transition: 0.2s; }
    .pricing-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.08); }
    .pricing-card .price { font-size: 2.5rem; font-weight: 700; color: #1e293b; margin: 0.5rem 0; }
    .pricing-card .price span { font-size: 1rem; font-weight: 400; color: #64748b; }
    .pricing-card ul { text-align: left; list-style: none; padding: 0; }
    .pricing-card ul li { padding: 4px 0; border-bottom: 1px solid #f1f5f9; }
    .pricing-card ul li:last-child { border-bottom: none; }
    .featured { border-color: #059669; position: relative; }
    .featured::before { content: "★ POPULAR"; position: absolute; top: -10px; right: -10px; background: #059669; color: white; padding: 2px 12px; border-radius: 20px; font-size: 0.7rem; font-weight: 700; }
    .team-card { background: white; padding: 1rem; border-radius: 12px; text-align: center; }
    .team-card img { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin-bottom: 0.5rem; border: 3px solid #e2e8f0; }
    .process-step { text-align: center; padding: 1rem; }
    .process-step .step-number { background-color: #3b82f6; color: white; width: 40px; height: 40px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: 700; }
    /* Header logo style - FIXED */
    .header-logo-img {
        height: 40px;
        width: auto;
        border-radius: 6px;
        max-height: 40px;
        object-fit: contain;
    }
    .header-container {
        display: flex;
        align-items: center;
        gap: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Helper functions
def save_order(name, email, phone, service, urgency, budget, description):
    file_path = "orders.csv"
    new_row = {"Date": datetime.now().strftime("%Y-%m-%d %H:%M"), "Name": name, "Email": email, "Phone": phone, "Service": service, "Urgency": urgency, "Budget": budget, "Description": description}
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])
    df.to_csv(file_path, index=False)

def save_message(name, email, message):
    file_path = "messages.csv"
    new_row = {"Date": datetime.now().strftime("%Y-%m-%d %H:%M"), "Name": name, "Email": email, "Message": message}
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])
    df.to_csv(file_path, index=False)

# ---- Logo path ----
logo_path = "Isabella_Website/logo.png/logo.png.png"

# ---- Generate header with properly sized logo ----
import base64
def get_image_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

if os.path.exists(logo_path):
    b64 = get_image_base64(logo_path)
    logo_img_html = f'<img src="data:image/png;base64,{b64}" class="header-logo-img" />'
else:
    # Fallback to text icon if logo not found
    logo_img_html = '<div style="font-size: 1.8rem; background: linear-gradient(135deg, #3b82f6, #8b5cf6); width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white;">✍️</div>'

# Header HTML with fixed logo size
header_html = f"""
<div style="position: sticky; top: 0; z-index: 999; background: white; padding: 8px 20px; border-bottom: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;">
    <div class="header-container">
        {logo_img_html}
        <div>
            <div style="font-size: 1.5rem; font-weight: 700; background: linear-gradient(135deg, #3b82f6, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Isabella</div>
            <div style="font-size: 0.65rem; color: #64748b;">Academic & Professional Writing</div>
        </div>
    </div>
    <a href="#order-now" style="background-color: #059669; color: white; border: none; padding: 6px 18px; border-radius: 30px; font-weight: 600; text-decoration: none; font-size: 0.9rem;">📝 Order Now</a>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

# Tabs
tabs = st.tabs(["🏠 Home", "📖 Services", "⚙️ How It Works", "💰 Pricing", "⭐ Testimonials", "👤 About", "❓ FAQ", "📞 Contact", "📝 Order Now"])
home_tab, services_tab, how_tab, pricing_tab, testimonials_tab, about_tab, faq_tab, contact_tab, order_tab = tabs

# ---------- HOME (unchanged) ----------
with home_tab:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("# Transform Your Ideas into Exceptional Writing\n**Premium academic and professional writing services tailored to your success.**\n\nGet expert assistance with essays, research papers, resumes, and more from our team of qualified professionals.")
        if st.button("Get a Free Quote"): st.info("Click on the 'Order Now' tab above.")
    with col2:
        st.image("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600", caption="Your success starts here", use_container_width=True)
    st.markdown('<div class="trust-badge"><p style="font-size: 1.1rem; color: #1e293b; margin: 0;">⭐ Trusted by students and professionals worldwide</p></div>', unsafe_allow_html=True)
    st.markdown("## What We Offer")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=400", caption="Academic Writing")
        st.markdown("**Essays, Research Papers, Dissertations** – from high school to PhD level.")
    with c2:
        st.image("https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=400", caption="Professional Writing")
        st.markdown("**Resumes, Cover Letters, Business Proposals** – get noticed by employers.")
    with c3:
        st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Website Development")
        st.markdown("**Custom Websites & Landing Pages** – build your online presence.")
    st.markdown("## How It Works")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="process-step"><div class="step-number">1</div><h4>Place Your Order</h4><p>Tell us about your project.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="process-step"><div class="step-number">2</div><h4>Get Matched</h4><p>We connect you with an expert.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="process-step"><div class="step-number">3</div><h4>Receive Your Work</h4><p>Get your polished document on time.</p></div>', unsafe_allow_html=True)

    st.markdown("## What Our Clients Say")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Isabella\'s team helped me with my dissertation when I was completely stuck. The quality was outstanding and delivered before deadline."</p><p class="author">— Sarah J., PhD Candidate</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"I used Isabella\'s resume writing service and landed an interview within a week. Highly recommend!"</p><p class="author">— Michael R., Marketing Executive</p></div>', unsafe_allow_html=True)

# ---------- SERVICES (unchanged) ----------
with services_tab:
    st.markdown("## Our Premium Services")
    st.image("https://images.unsplash.com/photo-1501504905252-473c47e087f8?w=800", caption="Excellence in every word", use_container_width=True)
    with st.expander("📚 Academic Writing", expanded=True):
        st.write("- **Essays & Assignments**: Well-researched, properly formatted.\n- **Research Papers**: In-depth analysis with credible sources.\n- **Dissertations & Theses**: Full support from proposal to submission.\n- **Coursework**: Assistance with projects and presentations.")
    with st.expander("💼 Professional Writing"):
        st.write("- **Resume/CV Writing**: ATS-friendly resumes.\n- **Cover Letters**: Tailored to your target job.\n- **Business Proposals**: Persuasive and results-driven.\n- **Editing & Proofreading**: Polished, error-free documents.")
    with st.expander("🌐 Website Development"):
        st.write("- **Custom Websites**: Built with Streamlit, HTML, CSS, or WordPress.\n- **Portfolio Sites**: Showcase your work.\n- **Landing Pages**: Convert visitors to clients.\n- **Maintenance & Support**: Ongoing updates and hosting.")
    st.info("All services are tailored to your needs. Contact us for a free quote!")

# ---------- HOW IT WORKS (unchanged) ----------
with how_tab:
    st.markdown("## How It Works")
    st.markdown("Our process is simple and transparent.")
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400", caption="Step 1: Place Your Order")
        st.markdown("**1. Fill out the order form** – Tell us what you need.")
    with c2:
        st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=400", caption="Step 2: Get Matched with an Expert")
        st.markdown("**2. We match you with a writer** – based on your subject and urgency.")
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1515378960530-7c0da6231fb1?w=400", caption="Step 3: Review & Communicate")
        st.markdown("**3. Collaborate with your writer** – give feedback and ask questions.")
    with c2:
        st.image("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=400", caption="Step 4: Receive Your Paper")
        st.markdown("**4. Get your final document** – ready for submission.")
    st.success("We guarantee 100% original, plagiarism‑free content.")

# ---------- PRICING (updated earlier) ----------
with pricing_tab:
    st.markdown("## Our Pricing")
    st.markdown("Transparent, per‑page rates for all your writing needs.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="pricing-card">
            <h3>Basic Essay</h3>
            <div class="price">$15 <span>/ page</span></div>
            <ul>
                <li>Standard essays & assignments</li>
                <li>3‑day delivery</li>
                <li>Free revisions</li>
                <li>Plagiarism report</li>
            </ul>
            <br>
            <a href="#order-now" style="text-decoration:none;">
                <button style="background:#3b82f6;color:white;border:none;padding:8px 20px;border-radius:30px;font-weight:600;cursor:pointer;">Choose</button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="pricing-card">
            <h3>Basic Dissertation</h3>
            <div class="price">$18 <span>/ page</span></div>
            <ul>
                <li>Dissertations & long research</li>
                <li>3‑day delivery</li>
                <li>Free revisions</li>
                <li>Plagiarism report</li>
            </ul>
            <br>
            <a href="#order-now" style="text-decoration:none;">
                <button style="background:#3b82f6;color:white;border:none;padding:8px 20px;border-radius:30px;font-weight:600;cursor:pointer;">Choose</button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="pricing-card featured">
            <h3>Urgent</h3>
            <div class="price">$20 <span>/ page</span></div>
            <ul>
                <li>Any type of paper</li>
                <li>24‑hour delivery</li>
                <li>Unlimited revisions</li>
                <li>Plagiarism report</li>
                <li>Direct chat with writer</li>
            </ul>
            <br>
            <a href="#order-now" style="text-decoration:none;">
                <button style="background:#059669;color:white;border:none;padding:8px 20px;border-radius:30px;font-weight:600;cursor:pointer;">Choose</button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="pricing-card">
            <h3>Premium</h3>
            <div class="price">$25 <span>/ page</span></div>
            <ul>
                <li>Highest quality</li>
                <li>12‑hour delivery</li>
                <li>Unlimited revisions</li>
                <li>Plagiarism report</li>
                <li>Direct chat + phone support</li>
                <li>Priority support</li>
            </ul>
            <br>
            <a href="#order-now" style="text-decoration:none;">
                <button style="background:#8b5cf6;color:white;border:none;padding:8px 20px;border-radius:30px;font-weight:600;cursor:pointer;">Choose</button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.caption("Prices are per page (approx. 300 words). Custom projects may vary. Contact us for a bespoke quote.")

# ---------- TESTIMONIALS (unchanged) ----------
with testimonials_tab:
    st.markdown("## Client Testimonials")
    st.markdown("Real stories from real clients.")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Isabella\'s team helped me with my dissertation when I was completely stuck. The quality was outstanding and delivered before deadline."</p><p class="author">— Sarah J., PhD Candidate</p></div><br><div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"I used Isabella\'s resume writing service and landed an interview within a week. Highly recommend!"</p><p class="author">— Michael R., Marketing Executive</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"The website they built for my business is gorgeous and converts well."</p><p class="author">— Amanda T., Small Business Owner</p></div><br><div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"I needed a last‑minute research paper and they saved me. The paper got an A."</p><p class="author">— David K., Undergraduate Student</p></div>', unsafe_allow_html=True)

# ---------- ABOUT (with Gilbert instead of Maria) ----------
with about_tab:
    st.markdown("## About Isabella")
    st.markdown("Your trusted partner in academic and professional success.")
    
    isabella_image_path = "Isabella_Website/logo.jsn/isabella photo.PNG"
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists(isabella_image_path):
            st.image(isabella_image_path, caption="Our Founder, Isabella", use_container_width=True)
        else:
            st.image("https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=400", caption="Our Founder, Isabella", use_container_width=True)
    with col2:
        st.markdown("""
        **Our Mission** – To empower students, professionals, and businesses with exceptional writing services that drive success.
        
        **Our Values** – Integrity, Quality, Confidentiality, and Customer Satisfaction.
        
        **Who We Are** – Isabella is a team of passionate writers, editors, and designers with years of experience across various fields. 
        We understand the pressure of deadlines and the importance of delivering work that exceeds expectations.
        
        We serve clients from all over the world, helping them achieve their academic and career goals.
        """)
    
    st.markdown("### Meet Our Core Team")
    col1, col2, col3 = st.columns(3)
    with col1:
        if os.path.exists(isabella_image_path):
            with st.container():
                st.image(isabella_image_path, width=120)
                st.markdown("""
                <h4 style="margin:0; text-align:center;">Isabella</h4>
                <p style="text-align:center; margin:0;">Founder & Lead Writer</p>
                <p style="font-size:0.8rem; color:#94a3b8; text-align:center;">PhD in English Literature</p>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="team-card">
                <img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=150">
                <h4>Isabella</h4>
                <p>Founder & Lead Writer</p>
                <p style="font-size:0.8rem;color:#94a3b8;">PhD in English Literature</p>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="team-card">
            <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?w=150">
            <h4>Sarah</h4>
            <p>Senior Academic Writer</p>
            <p style="font-size:0.8rem;color:#94a3b8;">MSc in Psychology</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        # ---- REPLACED Maria with Gilbert ----
        st.markdown("""
        <div class="team-card">
            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150">
            <h4>Gilbert</h4>
            <p>Technical Writing Specialist</p>
            <p style="font-size:0.8rem;color:#94a3b8;">BEng Electrical Engineering</p>
        </div>
        """, unsafe_allow_html=True)

# ---------- FAQ (unchanged) ----------
with faq_tab:
    st.markdown("## Frequently Asked Questions")
    with st.expander("What services do you offer?"):
        st.write("We offer academic writing, professional writing, and website development.")
    with st.expander("How do I place an order?"):
        st.write("Fill out the Order Form (click 'Order Now' tab).")
    with st.expander("Is my information kept confidential?"):
        st.write("Absolutely. We never share your personal data.")
    with st.expander("What if I need revisions?"):
        st.write("We offer free revisions until you are 100% satisfied.")
    with st.expander("How do you ensure quality?"):
        st.write("All work is written by experts, checked for plagiarism, and proofread.")
    with st.expander("What payment methods do you accept?"):
        st.write("We accept PayPal. See the Payment section in the Order Now tab.")

# ---------- CONTACT (unchanged) ----------
with contact_tab:
    st.title("📞 Contact Us")
    st.subheader("We're here to help")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Get in Touch\n\n📞 **Phone / WhatsApp:** +1 (775) 249-7692\n\n📧 **Email:** isabellajunior97@gmail.com\n\n🌐 **Website:** isabellawriting.com\n\n🕐 **Business Hours:** 24/7")
        st.markdown('<a href="https://wa.me/17752497692" target="_blank"><button style="background-color:#25D366;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">💬 Chat on WhatsApp</button></a>', unsafe_allow_html=True)
    with c2:
        st.markdown("### Send a Quick Message")
        with st.form("quick_contact", clear_on_submit=True):
            q_name = st.text_input("Your Name")
            q_email = st.text_input("Your Email")
            q_message = st.text_area("Message", height=100)
            q_submit = st.form_submit_button("Send Message")
            if q_submit and q_name and q_email and q_message:
                save_message(q_name, q_email, q_message)
                st.success("✅ Message sent! We'll get back to you soon.")
            elif q_submit:
                st.error("Please fill in all fields.")

# ---------- ORDER NOW (unchanged) ----------
with order_tab:
    st.title("📝 Place Your Order")
    st.subheader("Fill in the details below")
    with st.form("order_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name *", placeholder="e.g., John Doe")
            email = st.text_input("Email Address *", placeholder="john@example.com")
            phone = st.text_input("Phone Number", placeholder="+1 775 249 7692")
        with c2:
            service_type = st.selectbox("Service Type *", ["Select an option...", "Academic Writing", "Research Paper", "Dissertation/Thesis", "Resume/CV", "Cover Letter", "Business Proposal", "Website Development", "Editing/Proofreading", "Other"])
            urgency = st.selectbox("Urgency", ["Flexible", "Within 7 days", "Within 3 days", "Within 24 hours"])
            budget = st.number_input("Budget (USD)", min_value=0, step=10, value=50)
        description = st.text_area("Project Description *", placeholder="Describe your requirements...", height=150)
        file = st.file_uploader("Attach any relevant files (optional)", type=["pdf", "docx", "txt", "jpg", "png"])
        submitted = st.form_submit_button("📩 Submit Order Request")
        if submitted:
            if name and email and service_type != "Select an option..." and description:
                save_order(name, email, phone, service_type, urgency, budget, description)
                st.success("✅ Order submitted successfully!")
                st.info("We will contact you within 24 hours.")
                if file is not None:
                    st.write(f"📎 File attached: {file.name}")
            else:
                st.error("Please fill in all required fields (*).")
    st.caption("All information is kept strictly confidential.")
    st.markdown("---")
    st.subheader("💳 Make a Payment")
    st.markdown("After we discuss your project, you can pay securely via PayPal.")
    if 'show_payment' not in st.session_state:
        st.session_state.show_payment = False
    if st.button("🔒 Pay Now", key="pay_now_btn_order"):
        st.session_state.show_payment = not st.session_state.show_payment
    if st.session_state.show_payment:
        st.markdown('<div class="payment-details"><h3>Payment Information</h3><p><strong>PayPal Email:</strong> <code>muthokanzilu@gmail.com</code></p><p>Send your payment directly via PayPal.</p><p><a href="https://www.paypal.com/paypalme/muthokanzilu" target="_blank" style="background-color:#0070ba;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;font-weight:600;">💰 Go to PayPal.me</a></p><p style="font-size:0.9rem;color:#64748b;">You will be redirected to PayPal\'s secure site.</p></div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 Isabella Academic & Professional Writing Services")
