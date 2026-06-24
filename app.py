import streamlit as st
import pandas as pd
import os
from datetime import datetime
import base64

st.set_page_config(
    page_title="Isabella - Premium Academic & Professional Writing",
    page_icon="📚",
    layout="wide"
)

# ---------- HIDE STREAMLIT BRANDING ----------
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    .stAppDeployButton {display: none !important;}
    .stApp > header {display: none !important;}
    .stApp {
        padding-top: 0 !important;
    }
    .main > div {
        padding-top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Meta description for SEO
st.markdown("""
<head>
    <meta name="description" content="Expert academic & professional writing services. Order now and pay later. 24/7 support. Essays, resumes, dissertations, and more.">
</head>
""", unsafe_allow_html=True)

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
    .header-logo-img { height: 50px; width: auto; border-radius: 6px; max-height: 50px; object-fit: contain; }
    .header-container { display: flex; align-items: center; gap: 15px; }
    .payment-container { background: #f1f5f9; padding: 1.5rem; border-radius: 12px; text-align: center; margin: 1rem 0; }
    .payment-btn { background-color: #0070ba; color: white; border: none; padding: 14px 40px; border-radius: 30px; font-size: 18px; font-weight: 600; cursor: pointer; box-shadow: 0 4px 12px rgba(0,112,186,0.3); text-decoration: none; display: inline-block; }
    .payment-btn:hover { background-color: #005c9e; box-shadow: 0 6px 20px rgba(0,112,186,0.4); transform: translateY(-2px); }
    .admin-card { background: #f1f5f9; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 4px solid #3b82f6; }
    .chat-message-card { background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0; margin: 0.5rem 0; }
    .chat-message-card .client-name { font-weight: 600; color: #1e293b; }
    .chat-message-card .client-email { color: #64748b; font-size: 0.9rem; }
    .chat-message-card .message { margin: 0.5rem 0; color: #334155; }
    .chat-message-card .date { color: #94a3b8; font-size: 0.8rem; }

    .floating-chat {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 9999;
        background-color: #25D366;
        color: white;
        border: none;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        font-size: 28px;
        cursor: pointer;
        box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
    }
    .floating-chat:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 30px rgba(37, 211, 102, 0.5);
        background-color: #128C7E;
    }
    .floating-chat .tooltip {
        visibility: hidden;
        width: 140px;
        background-color: #1e293b;
        color: white;
        text-align: center;
        border-radius: 6px;
        padding: 6px 10px;
        position: absolute;
        right: 70px;
        font-size: 14px;
        font-weight: 400;
        opacity: 0;
        transition: opacity 0.3s;
        white-space: nowrap;
    }
    .floating-chat:hover .tooltip {
        visibility: visible;
        opacity: 1;
    }
    .floating-chat .tooltip::after {
        content: "";
        position: absolute;
        top: 50%;
        left: 100%;
        margin-top: -6px;
        border-width: 6px;
        border-style: solid;
        border-color: transparent transparent transparent #1e293b;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.4); }
        70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
        100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
    }
    .floating-chat.pulse { animation: pulse 2s infinite; }
    @media (max-width: 640px) {
        .floating-chat { width: 50px; height: 50px; font-size: 22px; bottom: 20px; right: 20px; }
        .floating-chat .tooltip { display: none; }
    }
</style>
""", unsafe_allow_html=True)

# ---------- FLOATING CHAT BUTTON ----------
st.markdown("""
<a href="https://wa.me/17752497692?text=Hi%20Isabella!%20I%20have%20a%20question%20about%20your%20services." target="_blank" class="floating-chat pulse" title="Chat on WhatsApp">
    💬
    <span class="tooltip">Chat on WhatsApp 💬</span>
</a>
""", unsafe_allow_html=True)

# ---------- HELPER FUNCTIONS ----------
def save_order(name, email, phone, service, urgency, budget, description, status="Pending"):
    file_path = "orders.csv"
    new_row = {"Date": datetime.now().strftime("%Y-%m-%d %H:%M"), "Name": name, "Email": email, "Phone": phone, "Service": service, "Urgency": urgency, "Budget": budget, "Description": description, "Status": status}
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])
    df.to_csv(file_path, index=False)
    return True

def save_message(name, email, message):
    file_path = "messages.csv"
    new_row = {"Date": datetime.now().strftime("%Y-%m-%d %H:%M"), "Name": name, "Email": email, "Message": message}
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])
    df.to_csv(file_path, index=False)
    return True

def save_chat(sender, name, email, message):
    file_path = "chats.csv"
    new_row = {"Date": datetime.now().strftime("%Y-%m-%d %H:%M"), "Sender": sender, "Name": name, "Email": email, "Message": message}
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])
    df.to_csv(file_path, index=False)
    return True

def get_orders():
    if os.path.exists("orders.csv"):
        return pd.read_csv("orders.csv")
    return pd.DataFrame()

def get_messages():
    if os.path.exists("messages.csv"):
        return pd.read_csv("messages.csv")
    return pd.DataFrame()

def get_chats():
    if os.path.exists("chats.csv"):
        return pd.read_csv("chats.csv")
    return pd.DataFrame()

# ---------- LOGO ----------
logo_path = "logo.png.png"

def get_image_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

if os.path.exists(logo_path):
    b64 = get_image_base64(logo_path)
    logo_img_html = f'<img src="data:image/png;base64,{b64}" class="header-logo-img" />'
else:
    logo_img_html = ""

header_html = f"""
<div style="position: sticky; top: 0; z-index: 999; background: white; padding: 10px 20px; border-bottom: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;">
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

# ---------- TABS ----------
tabs = st.tabs(["🏠 Home", "📖 Services", "⚙️ How It Works", "💰 Pricing", "⭐ Testimonials", "👤 About", "💬 Chat", "❓ FAQ", "📞 Contact", "📝 Order Now", "🔐 Admin"])
home_tab, services_tab, how_tab, pricing_tab, testimonials_tab, about_tab, chat_tab, faq_tab, contact_tab, order_tab, admin_tab = tabs

# ---------- HOME ----------
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

# ---------- SERVICES ----------
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

# ---------- HOW IT WORKS ----------
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

# ---------- PRICING ----------
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
    
    st.caption("Prices are per page (approx. 275 words). Custom projects may vary. Contact us for a bespoke quote.")
    
    st.markdown("---")
    st.markdown("""
    <div class="payment-container">
        <p style="font-size: 1.1rem; font-weight: 500; color: #1e293b;">
            💰 Ready to make a payment?
        </p>
        <p style="color: #64748b; margin-bottom: 1rem;">
            Payment is required after we've discussed your project and agreed on the final price.
        </p>
        <a href="https://www.paypal.com/paypalme/muthokanzilu" target="_blank" class="payment-btn">
            💳 Pay with PayPal
        </a>
        <p style="font-size:0.9rem; color:#64748b; margin-top:0.75rem;">
            You'll be redirected to PayPal's secure site.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- TESTIMONIALS ----------
with testimonials_tab:
    st.markdown("## Client Testimonials")
    st.markdown("Real stories from real clients.")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Isabella\'s team helped me with my dissertation when I was completely stuck. The quality was outstanding and delivered before deadline."</p><p class="author">— Sarah J., PhD Candidate</p></div><br><div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"I used Isabella\'s resume writing service and landed an interview within a week. Highly recommend!"</p><p class="author">— Michael R., Marketing Executive</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"The website they built for my business is gorgeous and converts well."</p><p class="author">— Amanda T., Small Business Owner</p></div><br><div class="testimonial-card"><div class="stars">⭐⭐⭐⭐⭐</div><p>"I needed a last‑minute research paper and they saved me. The paper got an A."</p><p class="author">— David K., Undergraduate Student</p></div>', unsafe_allow_html=True)

# ---------- ABOUT ----------
with about_tab:
    st.markdown("## About Isabella")
    st.markdown("Your trusted partner in academic and professional success.")
    
    isabella_image_path = "isabella.png.PNG"
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists(isabella_image_path):
            st.image(isabella_image_path, caption="Our Founder, Isabella", use_container_width=True)
        else:
            st.markdown("*(Isabella's photo will appear here)*")
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
        st.markdown("""
        <div class="team-card">
            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150">
            <h4>Gilbert</h4>
            <p>Technical Writing Specialist</p>
            <p style="font-size:0.8rem;color:#94a3b8;">BEng Electrical Engineering</p>
        </div>
        """, unsafe_allow_html=True)

# ---------- CHAT ----------
with chat_tab:
    st.title("💬 Chat with Admin")
    st.subheader("Have questions before placing your order? Chat with us!")
    
    st.info("We'll respond as soon as possible. Feel free to ask about pricing, deadlines, or any special requirements.")
    
    st.markdown("""
    <div style="background-color: #f1f5f9; padding: 1.5rem; border-radius: 12px; text-align: center; margin: 1rem 0;">
        <p style="font-size: 1.2rem; font-weight: 600; color: #1e293b;">💬 Start Chatting Now</p>
        <p style="color: #64748b;">Click the button below to chat with us instantly on WhatsApp.</p>
        <a href="https://wa.me/17752497692?text=Hi%20Isabella!%20I%20have%20a%20question%20about%20your%20services." target="_blank">
            <button style="background-color:#25D366;color:white;border:none;padding:12px 30px;border-radius:30px;font-size:18px;font-weight:600;cursor:pointer;box-shadow:0 4px 12px rgba(37,211,102,0.3);">
                💬 Chat Now on WhatsApp
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Or send us a message using the form below")
    
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            chat_name = st.text_input("Your Name *", placeholder="e.g., John Doe")
        with col2:
            chat_email = st.text_input("Your Email *", placeholder="john@example.com")
        
        chat_message = st.text_area("Your Message *", placeholder="Write your question or inquiry here...", height=120)
        
        chat_submit = st.form_submit_button("💬 Send Message to Admin")
        
        if chat_submit:
            if chat_name and chat_email and chat_message:
                save_chat("Client", chat_name, chat_email, chat_message)
                st.success("✅ Message sent! We'll get back to you soon.")
                
                whatsapp_notify = f"Hi Isabella! New chat message from {chat_name}%0A%0A"
                whatsapp_notify += f"📧 Email: {chat_email}%0A"
                whatsapp_notify += f"💬 Message: {chat_message[:150]}..."
                whatsapp_notify += f"%0A%0A📱 Reply to them from your Admin Dashboard: https://isabella-writing.streamlit.app/#admin"
                
                st.markdown(f"""
                <div style="background-color: #f1f5f9; padding: 1rem; border-radius: 12px; margin: 1rem 0;">
                    <p style="font-weight: 600; color: #1e293b;">📱 Notify Admin on WhatsApp:</p>
                    <p style="font-size: 0.9rem; color: #64748b;">Click the button below to notify the admin about this message.</p>
                    <a href="https://wa.me/17752497692?text={whatsapp_notify}" target="_blank">
                        <button style="background-color:#25D366;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
                            📱 Send Notification
                        </button>
                    </a>
                </div>
                """, unsafe_allow_html=True)
                
                st.info("📱 You can also reach us on WhatsApp for immediate response.")
            else:
                st.error("Please fill in all required fields (*).")

# ---------- FAQ ----------
with faq_tab:
    st.markdown("## Frequently Asked Questions")
    with st.expander("What services do you offer?"):
        st.write("We offer academic writing, professional writing, and website development.")
    with st.expander("How do I place an order?"):
        st.write("Fill out the Order Form (click 'Order Now' tab). You can pay after we discuss your project.")
    with st.expander("Is my information kept confidential?"):
        st.write("Absolutely. We never share your personal data.")
    with st.expander("What if I need revisions?"):
        st.write("We offer free revisions until you are 100% satisfied.")
    with st.expander("How do you ensure quality?"):
        st.write("All work is written by experts, checked for plagiarism, and proofread.")
    with st.expander("Do I need to pay before submitting an order?"):
        st.write("No! You can submit your order first, and we'll discuss the project before any payment is required.")
    with st.expander("What payment methods do you accept?"):
        st.write("We accept PayPal. You can pay using the 'Pay with PayPal' button after we agree on the price.")

# ---------- CONTACT ----------
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

# ---------- ORDER NOW ----------
with order_tab:
    st.title("📝 Place Your Order")
    st.subheader("Fill in the details below")
    
    st.info("💡 **You don't need to pay upfront!** Submit your order, and we'll discuss your project and pricing before any payment is required.")
    
    with st.form("order_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name *", placeholder="e.g., John Doe")
            email = st.text_input("Email Address *", placeholder="john@example.com")
            phone = st.text_input("Phone Number *", placeholder="+1 775 249 7692")
        with c2:
            service_type = st.selectbox("Service Type *", ["Select an option...", "Academic Writing", "Research Paper", "Dissertation/Thesis", "Resume/CV", "Cover Letter", "Business Proposal", "Website Development", "Editing/Proofreading", "Other"])
            urgency = st.selectbox("Urgency", ["Flexible", "Within 7 days", "Within 3 days", "Within 24 hours"])
            budget = st.number_input("Estimated Budget (USD)", min_value=0, step=10, value=50, help="This is an estimate – we'll discuss final pricing later.")
        
        description = st.text_area("Project Description *", placeholder="Describe your requirements in detail...", height=150)
        
        file = st.file_uploader("Attach any relevant files (optional)", type=["pdf", "docx", "txt", "jpg", "png"])
        
        submitted = st.form_submit_button("📩 Submit Order Request")
        
        if submitted:
            if name and email and phone and service_type != "Select an option..." and description:
                save_order(name, email, phone, service_type, urgency, budget, description)
                st.success("✅ Order submitted successfully!")
                st.info("We will contact you within 24 hours to discuss your project and provide a quote.")
                
                whatsapp_msg = f"Hi Isabella! New order from {name}%0A%0A"
                whatsapp_msg += f"📝 Service: {service_type}%0A"
                whatsapp_msg += f"⏰ Urgency: {urgency}%0A"
                whatsapp_msg += f"💰 Budget: ${budget}%0A"
                whatsapp_msg += f"📧 Email: {email}%0A"
                whatsapp_msg += f"📱 Phone: {phone}%0A%0A"
                whatsapp_msg += f"📄 Description: {description[:100]}..."
                
                st.markdown(f"""
                <div style="background-color: #f1f5f9; padding: 1rem; border-radius: 12px; margin: 1rem 0;">
                    <p style="font-weight: 600; color: #1e293b;">📱 Notify Admin on WhatsApp:</p>
                    <p style="font-size: 0.9rem; color: #64748b;">Click the button below to send order details to the admin on WhatsApp.</p>
                    <a href="https://wa.me/17752497692?text={whatsapp_msg}" target="_blank">
                        <button style="background-color:#25D366;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
                            📱 Send Order Notification
                        </button>
                    </a>
                </div>
                """, unsafe_allow_html=True)
                
                if file is not None:
                    st.write(f"📎 File attached: {file.name}")
            else:
                st.error("Please fill in all required fields (*).")
    
    st.caption("All information is kept strictly confidential. You will receive a quote before any payment is required.")
    
    st.markdown("---")
    st.markdown("""
    <div class="payment-container">
        <p style="font-size: 1.2rem; font-weight: 600; color: #1e293b;">
            💰 Ready to complete your payment?
        </p>
        <p style="color: #64748b; margin-bottom: 1rem;">
            Payment is required <strong>after</strong> we've discussed your project and agreed on the final price.
        </p>
        <a href="https://www.paypal.com/paypalme/muthokanzilu" target="_blank" class="payment-btn">
            💳 Pay with PayPal
        </a>
        <p style="font-size:0.9rem; color:#64748b; margin-top:0.75rem;">
            You'll be redirected to PayPal's secure site.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- ADMIN DASHBOARD ----------
with admin_tab:
    st.title("🔐 Admin Dashboard")
    st.subheader("Manage orders and client communications")
    
    admin_password = "admin123"  # Change this to your own password
    
    if 'admin_logged_in' not in st.session_state:
        st.session_state.admin_logged_in = False
    
    if not st.session_state.admin_logged_in:
        with st.form("admin_login"):
            password = st.text_input("Enter Admin Password", type="password")
            login_submit = st.form_submit_button("Login")
            if login_submit:
                if password == admin_password:
                    st.session_state.admin_logged_in = True
                    st.success("✅ Logged in successfully!")
                    st.rerun()
                else:
                    st.error("❌ Incorrect password")
    else:
        st.success("✅ Logged in as Admin")
        if st.button("Logout"):
            st.session_state.admin_logged_in = False
            st.rerun()
        
        st.markdown("---")
        
        # ORDERS
        st.markdown("### 📋 Recent Orders")
        orders_df = get_orders()
        if not orders_df.empty:
            st.dataframe(orders_df, use_container_width=True)
            csv = orders_df.to_csv(index=False)
            st.download_button("📥 Download Orders as CSV", data=csv, file_name="orders.csv", mime="text/csv")
            
            st.markdown("#### ✉️ Contact Clients")
            for idx, row in orders_df.iterrows():
                with st.container():
                    col1, col2, col3 = st.columns([2, 2, 1])
                    with col1:
                        st.markdown(f"**{row['Name']}** – {row['Service']}")
                        st.caption(f"📧 {row['Email']} | 📱 {row['Phone']}")
                    with col2:
                        st.caption(f"📝 {row['Description'][:80]}...")
                    with col3:
                        reply_msg = f"Hi {row['Name']}! I received your order for {row['Service']}. Let's discuss your project."
                        st.markdown(f'<a href="https://wa.me/{row["Phone"]}?text={reply_msg.replace(" ", "%20")}" target="_blank"><button style="background-color:#25D366;color:white;border:none;padding:6px 12px;border-radius:6px;font-size:12px;cursor:pointer;">💬 Reply</button></a>', unsafe_allow_html=True)
                    st.markdown("---")
        else:
            st.info("No orders yet.")
        
        st.markdown("---")
        
        # CHAT MESSAGES
        st.markdown("### 💬 Client Chat Messages")
        chats_df = get_chats()
        if not chats_df.empty:
            for idx, row in chats_df.iterrows():
                with st.container():
                    st.markdown(f"""
                    <div class="chat-message-card">
                        <div class="client-name">{row['Name']}</div>
                        <div class="client-email">{row['Email']} • {row['Date']}</div>
                        <div class="message">💬 {row['Message']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2 = st.columns([4, 1])
                    with col2:
                        reply_msg = f"Hi {row['Name']}! Thanks for your message. "
                        client_question = row['Message'][:100]
                        st.markdown(f'<a href="https://wa.me/17752497692?text=Hi%20{row["Name"]}%2C%20I%20received%20your%20message%20about%3A%20{client_question.replace(" ", "%20")}..." target="_blank"><button style="background-color:#25D366;color:white;border:none;padding:6px 12px;border-radius:6px;font-size:12px;cursor:pointer;">💬 Reply via WhatsApp</button></a>', unsafe_allow_html=True)
                    st.markdown("---")
        else:
            st.info("No chat messages yet.")
        
        st.markdown("---")
        
        # CONTACT FORM MESSAGES
        st.markdown("### 📩 Contact Form Messages")
        messages_df = get_messages()
        if not messages_df.empty:
            for idx, row in messages_df.iterrows():
                with st.container():
                    st.markdown(f"""
                    <div class="chat-message-card">
                        <div class="client-name">{row['Name']}</div>
                        <div class="client-email">{row['Email']} • {row['Date']}</div>
                        <div class="message">💬 {row['Message']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2 = st.columns([4, 1])
                    with col2:
                        reply_msg = f"Hi {row['Name']}! Thanks for contacting us. "
                        client_question = row['Message'][:100]
                        st.markdown(f'<a href="https://wa.me/17752497692?text=Hi%20{row["Name"]}%2C%20I%20received%20your%20message%20about%3A%20{client_question.replace(" ", "%20")}..." target="_blank"><button style="background-color:#25D366;color:white;border:none;padding:6px 12px;border-radius:6px;font-size:12px;cursor:pointer;">💬 Reply via WhatsApp</button></a>', unsafe_allow_html=True)
                    st.markdown("---")
        else:
            st.info("No contact messages yet.")
        
        st.markdown("---")
        st.info(f"📱 WhatsApp: +1 (775) 249-7692 | 📧 Email: isabellajunior97@gmail.com")

st.markdown("---")
st.caption("© 2026 Isabella Academic & Professional Writing Services")
