"""
ESGx.Africa - Enhanced Platform Demo with Strategic Recommendations
AI-Powered ESG Intelligence for Africa with Ubuntu Philosophy
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import json

# Page configuration
st.set_page_config(
    page_title="ESGx.Africa - Ubuntu ESG Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1c7e57;
        text-align: center;
        margin-bottom: 1rem;
    }
    .ubuntu-card {
        background: linear-gradient(135deg, #1c7e57, #28a85c);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1c7e57;
        margin: 0.5rem 0;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .recommendation-card {
        background: #e8f5e8;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a85c;
        margin: 0.5rem 0;
    }
    .partnership-card {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 0.5rem 0;
    }
    .mobile-optimized {
        border: 2px solid #007bff;
        border-radius: 10px;
        padding: 1rem;
        background: #f0f8ff;
    }
</style>
""", unsafe_allow_html=True)

# Main header with enhanced branding
st.markdown('<h1 class="main-header">🌍 ESGx.Africa</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Africa\'s Premier AI-Powered ESG Platform | Ubuntu Philosophy Integrated | Production Ready</p>', unsafe_allow_html=True)

# Enhanced sidebar navigation
st.sidebar.image("https://via.placeholder.com/200x80/1c7e57/ffffff?text=ESGx.Africa+v2.0", width=200)
st.sidebar.markdown("### 🚀 **Enhanced Platform Features**")

page = st.sidebar.selectbox(
    "Navigate to:",
    ["🏠 Enhanced Dashboard", "📊 Ubuntu ESG Calculator", "🤖 AI ESG Agents", "📈 Analytics & Reports", 
     "🏢 Organization Profile", "💰 Subscription Plans", "🎓 ESGx Academy", "🌱 Carbon Accounting",
     "🛰️ Satellite Monitoring", "📱 Mobile Platform", "🤝 Community Hub", "💼 Investment Tracker",
     "🔗 API Marketplace", "📋 Strategic Recommendations"]
)

# Sample enhanced data
sample_org_data = {
    "name": "Ubuntu Mining Corp",
    "country": "South Africa",
    "industry": "Mining",
    "employees": 2500,
    "subscription": "Growth Pro",
    "ubuntu_rating": "Ubuntu Champion",
    "partnerships": ["AfDB", "JSE", "Traditional Authority"],
    "certifications": ["ISO 14001", "BEE Level 3", "Ubuntu Certified"]
}

# Enhanced Home Dashboard
if page == "🏠 Enhanced Dashboard":
    
    # Welcome message with recommendations
    st.markdown("""
    <div class="ubuntu-card">
        <h2>🌟 Welcome to ESGx.Africa Enhanced Platform</h2>
        <p>Africa's most comprehensive AI-powered ESG platform now with satellite monitoring, mobile optimization, and community features.</p>
        <p><strong>Ubuntu:</strong> "I am because we are" - Community-centered sustainability enhanced with cutting-edge technology.</p>
        <p><strong>NEW:</strong> Real-time satellite data, mobile apps, API marketplace, and investment tracking!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced key metrics with new features
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="Overall ESG Score",
            value="82.4",
            delta="↑ 7.1 vs last quarter",
            help="Enhanced with satellite data and AI predictions"
        )
    
    with col2:
        st.metric(
            label="Ubuntu Index™",
            value="87.2",
            delta="↑ 12.3 vs last quarter", 
            help="Community-verified with traditional leaders council"
        )
    
    with col3:
        st.metric(
            label="Satellite Verified",
            value="✅ Real-time",
            delta="🛰️ New Feature",
            help="Live satellite monitoring of environmental metrics"
        )
    
    with col4:
        st.metric(
            label="Mobile Users",
            value="1,247",
            delta="↑ 340% growth",
            help="Mobile-first platform adoption"
        )
    
    with col5:
        st.metric(
            label="API Calls/Day",
            value="45.2K",
            delta="↑ 89% integration",
            help="Third-party platform integrations"
        )
    
    # Enhanced features showcase
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚀 New Platform Enhancements")
        
        enhancements = [
            {
                "feature": "🛰️ Satellite Integration",
                "description": "Real-time environmental monitoring via NASA/ESA data",
                "status": "Live",
                "impact": "40% more accurate environmental scores"
            },
            {
                "feature": "📱 Mobile-First Design", 
                "description": "Native iOS/Android apps with offline capabilities",
                "status": "Beta",
                "impact": "300% increase in rural user adoption"
            },
            {
                "feature": "🤝 Community Verification",
                "description": "Traditional leaders validate Ubuntu initiatives",
                "status": "Live",
                "impact": "95% community trust score"
            },
            {
                "feature": "🔗 API Marketplace",
                "description": "200+ ESG data integrations available",
                "status": "Live", 
                "impact": "80% faster compliance reporting"
            }
        ]
        
        for enhancement in enhancements:
            st.markdown(f"""
            <div class="recommendation-card">
                <strong>{enhancement['feature']}</strong><br>
                {enhancement['description']}<br>
                <small style="color: #28a85c;">Status: {enhancement['status']} | Impact: {enhancement['impact']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🤝 Strategic Partnerships")
        
        partnerships = [
            {
                "partner": "African Development Bank",
                "type": "Financial Institution",
                "benefit": "R50M ESG investment pipeline access",
                "status": "Active"
            },
            {
                "partner": "Traditional Leaders Council",
                "type": "Cultural Authority", 
                "benefit": "Ubuntu authenticity certification",
                "status": "Advisory Board"
            },
            {
                "partner": "JSE Limited",
                "type": "Stock Exchange",
                "benefit": "Direct compliance reporting",
                "status": "Integration Live"
            },
            {
                "partner": "NASA Earth Observatory",
                "type": "Technology Partner",
                "benefit": "Satellite environmental data",
                "status": "Data Feed Active"
            }
        ]
        
        for partnership in partnerships:
            st.markdown(f"""
            <div class="partnership-card">
                <strong>{partnership['partner']}</strong><br>
                {partnership['type']}<br>
                <small style="color: #856404;">Benefit: {partnership['benefit']}</small><br>
                <small style="color: #856404;">Status: {partnership['status']}</small>
            </div>
            """, unsafe_allow_html=True)

# New Satellite Monitoring Page
elif page == "🛰️ Satellite Monitoring":
    
    st.header("🛰️ Real-Time Satellite Environmental Monitoring")
    st.markdown("**Live satellite data integration for accurate environmental ESG scoring**")
    
    # Satellite data dashboard
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Forest Cover", "2,847 ha", "↓ 12 ha this month")
    
    with col2:
        st.metric("Water Quality", "82% Clean", "↑ 5% improvement")
    
    with col3:
        st.metric("Air Quality Index", "45 Good", "↓ 8 points improved")
    
    with col4:
        st.metric("Land Use Change", "0.3%", "↓ Reduced degradation")
    
    # Satellite visualization
    st.subheader("📊 Environmental Monitoring Dashboard")
    
    # Create sample satellite data visualization
    dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
    satellite_data = pd.DataFrame({
        'Date': dates,
        'Forest_Cover': 2860 - np.cumsum(np.random.normal(0.5, 0.2, len(dates))),
        'Water_Quality': 78 + np.cumsum(np.random.normal(0.1, 0.5, len(dates))),
        'Air_Quality': 50 - np.cumsum(np.random.normal(0.2, 0.3, len(dates))),
        'Carbon_Absorption': 45 + np.random.normal(0, 2, len(dates))
    })
    
    fig = px.line(satellite_data, x='Date', 
                  y=['Forest_Cover', 'Water_Quality', 'Air_Quality'],
                  title='Real-Time Satellite Environmental Monitoring')
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Satellite alerts
    st.subheader("🚨 Environmental Alerts")
    
    alerts = [
        {"severity": "Medium", "alert": "Deforestation detected in Sector 7", "action": "Deploy monitoring team"},
        {"severity": "Low", "alert": "Water turbidity increase in River Basin A", "action": "Schedule water quality test"},
        {"severity": "High", "alert": "Illegal mining activity detected", "action": "Alert authorities immediately"}
    ]
    
    for alert in alerts:
        color = "#dc3545" if alert["severity"] == "High" else "#ffc107" if alert["severity"] == "Medium" else "#28a745"
        st.markdown(f"""
        <div class="metric-card" style="border-left-color: {color};">
            <strong style="color: {color};">{alert['severity']} Priority</strong><br>
            {alert['alert']}<br>
            <small>Recommended Action: {alert['action']}</small>
        </div>
        """, unsafe_allow_html=True)

# Mobile Platform Page
elif page == "📱 Mobile Platform":
    
    st.header("📱 Mobile-First ESG Platform")
    st.markdown("**Optimized for African connectivity and mobile-first users**")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="mobile-optimized">
            <h3>📱 Mobile App Features</h3>
            <ul>
                <li><strong>Offline Mode:</strong> Work without internet, sync when connected</li>
                <li><strong>Low Bandwidth:</strong> Optimized for 2G/3G networks</li>
                <li><strong>Voice Interface:</strong> ESG reporting in local languages</li>
                <li><strong>SMS Integration:</strong> Receive alerts and submit basic data</li>
                <li><strong>WhatsApp Bot:</strong> AI ESG assistant via WhatsApp</li>
                <li><strong>QR Code Reports:</strong> Share ESG scores instantly</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Mobile usage statistics
        st.subheader("📊 Mobile Usage Statistics")
        
        mobile_stats = {
            'Platform': ['Mobile App', 'WhatsApp Bot', 'SMS', 'Web Mobile', 'Desktop'],
            'Users': [1247, 892, 634, 543, 287],
            'Engagement': [85, 92, 78, 65, 45]
        }
        
        df_mobile = pd.DataFrame(mobile_stats)
        
        fig = px.bar(df_mobile, x='Platform', y=['Users', 'Engagement'],
                     title='Platform Usage and Engagement',
                     barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📲 Mobile Demo")
        
        # Simulate mobile interface
        st.markdown("**WhatsApp ESG Bot Demo**")
        
        # Chat simulation
        chat_messages = [
            {"role": "user", "message": "What's my Ubuntu score?"},
            {"role": "bot", "message": "Your current Ubuntu Index is 87.2 🎉\n\nBreakdown:\n• Community Engagement: 92%\n• Local Procurement: 78%\n• Cultural Preservation: 88%"},
            {"role": "user", "message": "How can I improve?"},
            {"role": "bot", "message": "Recommendations for higher Ubuntu score:\n\n1. Increase local procurement by 5%\n2. Start 1 new community project\n3. Document traditional practices\n\nWould you like specific guidance? 🤝"}
        ]
        
        for msg in chat_messages:
            if msg["role"] == "user":
                st.markdown(f"**You:** {msg['message']}")
            else:
                st.markdown(f"**Ubuntu Bot:** {msg['message']}")
                
        # Mobile metrics
        st.subheader("📈 Mobile Impact")
        st.metric("Rural Users", "68%", "↑ 45% vs desktop")
        st.metric("Offline Usage", "34%", "Critical for remote areas")
        st.metric("Local Language", "52%", "↑ 28% engagement")

# Community Hub Page
elif page == "🤝 Community Hub":
    
    st.header("🤝 Ubuntu Community Network")
    st.markdown("**Connect ESG practitioners across Africa with Ubuntu philosophy**")
    
    # Community metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Active Members", "12,847", "↑ 23% this month")
    
    with col2:
        st.metric("Ubuntu Champions", "324", "Community leaders")
    
    with col3:
        st.metric("Knowledge Shared", "1,892", "Best practices posted")
    
    with col4:
        st.metric("Mentorship Matches", "567", "Experienced-emerging pairs")
    
    # Community features
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌍 Regional Chapters")
        
        chapters = [
            {"region": "Southern Africa", "members": 4234, "lead": "Dr. Nomsa Mbeki", "focus": "Mining ESG"},
            {"region": "East Africa", "members": 3456, "lead": "Prof. James Mwangi", "focus": "Agricultural Sustainability"},
            {"region": "West Africa", "members": 2987, "lead": "Dr. Amina Kone", "focus": "Oil & Gas ESG"},
            {"region": "Central Africa", "members": 1456, "lead": "Dr. Jean Baptiste", "focus": "Forest Conservation"},
            {"region": "North Africa", "members": 714, "lead": "Dr. Omar Hassan", "focus": "Renewable Energy"}
        ]
        
        for chapter in chapters:
            with st.expander(f"{chapter['region']} - {chapter['members']} members"):
                st.markdown(f"**Chapter Lead:** {chapter['lead']}")
                st.markdown(f"**Focus Area:** {chapter['focus']}")
                st.markdown(f"**Members:** {chapter['members']}")
                if st.button(f"Join {chapter['region']}", key=f"join_{chapter['region']}"):
                    st.success(f"✅ Joined {chapter['region']} chapter!")
    
    with col2:
        st.subheader("📚 Knowledge Exchange")
        
        knowledge_items = [
            {
                "title": "Ubuntu-Centered Mining Practices",
                "author": "Ubuntu Mining Corp",
                "type": "Case Study",
                "rating": 4.8,
                "downloads": 1234
            },
            {
                "title": "Community Engagement Framework",
                "author": "Dr. Thabo Mofokeng",
                "type": "Research Paper",
                "rating": 4.9,
                "downloads": 987
            },
            {
                "title": "BEE Compliance Automation",
                "author": "JSE ESG Team",
                "type": "Technical Guide",
                "rating": 4.7,
                "downloads": 756
            },
            {
                "title": "Traditional Knowledge in ESG",
                "author": "Traditional Leaders Council",
                "type": "Philosophy Guide",
                "rating": 5.0,
                "downloads": 2134
            }
        ]
        
        for item in knowledge_items:
            with st.expander(f"⭐ {item['rating']} - {item['title']}"):
                st.markdown(f"**Author:** {item['author']}")
                st.markdown(f"**Type:** {item['type']}")
                st.markdown(f"**Downloads:** {item['downloads']}")
                if st.button(f"Download", key=f"download_{item['title']}"):
                    st.success("📄 Downloaded successfully!")

# Investment Tracker Page
elif page == "💼 Investment Tracker":
    
    st.header("💼 ESG Investment & Impact Tracking")
    st.markdown("**Track ESG investments, funding, and financial impact across Africa**")
    
    # Investment metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total ESG Funding", "R2.4B", "↑ 67% YoY growth")
    
    with col2:
        st.metric("Active Investors", "147", "Development finance + private")
    
    with col3:
        st.metric("Funded Projects", "892", "Ubuntu-verified initiatives")
    
    with col4:
        st.metric("Communities Impacted", "245K", "Direct beneficiaries")
    
    # Investment opportunities
    st.subheader("🎯 ESG Investment Opportunities")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📈 Trending ESG Investments**")
        
        investments = [
            {
                "project": "Solar Microgrids - Rural Kenya",
                "amount": "R45M",
                "investor": "African Development Bank",
                "ubuntu_score": 94,
                "expected_return": "12% IRR",
                "impact": "15K people electrified"
            },
            {
                "project": "Sustainable Mining - Ghana",
                "amount": "R120M", 
                "investor": "IFC + Local Partners",
                "ubuntu_score": 87,
                "expected_return": "15% IRR",
                "impact": "Local community ownership"
            },
            {
                "project": "Green Bonds - South Africa",
                "amount": "R200M",
                "investor": "JSE Green Bond Fund",
                "ubuntu_score": 91,
                "expected_return": "8% Fixed",
                "impact": "Carbon neutral by 2030"
            }
        ]
        
        for inv in investments:
            with st.expander(f"{inv['project']} - {inv['amount']}"):
                st.markdown(f"**Investor:** {inv['investor']}")
                st.markdown(f"**Ubuntu Score:** {inv['ubuntu_score']}/100")
                st.markdown(f"**Expected Return:** {inv['expected_return']}")
                st.markdown(f"**Impact:** {inv['impact']}")
                if st.button(f"Express Interest", key=f"invest_{inv['project']}"):
                    st.success("📧 Interest registered! Investor will contact you.")
    
    with col2:
        st.markdown("**💰 Funding Sources**")
        
        funding_sources = {
            'Source': ['Development Finance', 'Private Equity', 'Green Bonds', 'Impact Funds', 'Government'],
            'Amount (R Billions)': [0.8, 0.6, 0.4, 0.3, 0.3],
            'Projects': [45, 32, 28, 67, 23]
        }
        
        df_funding = pd.DataFrame(funding_sources)
        
        fig = px.pie(df_funding, values='Amount (R Billions)', names='Source',
                     title='ESG Funding Sources Distribution')
        st.plotly_chart(fig, use_container_width=True)
        
        # ROI tracking
        st.markdown("**📊 ESG Investment ROI**")
        
        roi_data = {
            'Metric': ['Financial Return', 'Social Impact', 'Environmental Benefit', 'Ubuntu Integration'],
            'Score': [85, 92, 88, 94]
        }
        
        df_roi = pd.DataFrame(roi_data)
        
        fig_roi = px.bar(df_roi, x='Metric', y='Score',
                         title='ESG Investment Impact Scores',
                         color='Score',
                         color_continuous_scale='Greens')
        st.plotly_chart(fig_roi, use_container_width=True)

# API Marketplace Page
elif page == "🔗 API Marketplace":
    
    st.header("🔗 ESG API Marketplace & Integrations")
    st.markdown("**200+ ESG data sources and integrations for seamless platform connectivity**")
    
    # API metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Available APIs", "247", "Curated ESG data sources")
    
    with col2:
        st.metric("Active Integrations", "89", "Live data feeds")
    
    with col3:
        st.metric("Daily API Calls", "1.2M", "↑ 340% growth")
    
    with col4:
        st.metric("Data Accuracy", "96.7%", "AI-verified quality")
    
    # API categories
    api_categories = {
        "🌍 Environmental Data": [
            {"name": "NASA Earth Observatory", "desc": "Satellite environmental monitoring", "price": "Free", "calls": "1M/month"},
            {"name": "Weather API Africa", "desc": "Climate and weather data", "price": "$0.001/call", "calls": "100K/month"},
            {"name": "Carbon Credit Registry", "desc": "African carbon offset data", "price": "$0.01/call", "calls": "50K/month"}
        ],
        "👥 Social Impact Data": [
            {"name": "UNDP Human Development", "desc": "Social development metrics", "price": "Free", "calls": "500K/month"},
            {"name": "African Employment Stats", "desc": "Labor and employment data", "price": "$0.005/call", "calls": "200K/month"},
            {"name": "Community Engagement API", "desc": "Ubuntu philosophy metrics", "price": "$0.02/call", "calls": "75K/month"}
        ],
        "🏛️ Governance & Compliance": [
            {"name": "BEE Verification API", "desc": "Real-time BEE compliance", "price": "$0.05/call", "calls": "25K/month"},
            {"name": "JSE Sustainability Feed", "desc": "Stock exchange ESG data", "price": "$0.10/call", "calls": "10K/month"},
            {"name": "African Regulatory DB", "desc": "Multi-country compliance", "price": "$0.03/call", "calls": "50K/month"}
        ]
    }
    
    for category, apis in api_categories.items():
        st.subheader(category)
        
        cols = st.columns(len(apis))
        for i, api in enumerate(apis):
            with cols[i]:
                with st.container():
                    st.markdown(f"**{api['name']}**")
                    st.markdown(f"{api['desc']}")
                    st.markdown(f"**Price:** {api['price']}")
                    st.markdown(f"**Usage:** {api['calls']}")
                    if st.button(f"Integrate", key=f"api_{api['name']}"):
                        st.success(f"✅ {api['name']} integrated!")

# Strategic Recommendations Page
elif page == "📋 Strategic Recommendations":
    
    st.header("📋 Strategic Implementation Roadmap")
    st.markdown("**Comprehensive recommendations for platform growth and market leadership**")
    
    # Implementation timeline
    st.subheader("🗓️ 90-Day Sprint Plan")
    
    timeline_data = {
        "Phase": ["Week 1-2", "Week 3-4", "Week 5-8", "Week 9-12"],
        "Focus": ["Market Validation", "Partnership Development", "Product Enhancement", "Scale Preparation"],
        "Key Deliverables": [
            "10 paying pilot customers",
            "AfDB & JSE partnerships signed",
            "Mobile app beta launch",
            "Series A pitch deck ready"
        ],
        "Success Metrics": [
            "R500K ARR committed",
            "2 major partnerships",
            "1K mobile users",
            "R20M funding target"
        ]
    }
    
    timeline_df = pd.DataFrame(timeline_data)
    
    for i, row in timeline_df.iterrows():
        with st.expander(f"{row['Phase']}: {row['Focus']}"):
            st.markdown(f"**Key Deliverable:** {row['Key Deliverables']}")
            st.markdown(f"**Success Metric:** {row['Success Metrics']}")
    
    # Priority recommendations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚀 High Priority Actions")
        
        high_priority = [
            {
                "action": "Ubuntu Philosophy Council",
                "rationale": "Ensure authentic Ubuntu integration",
                "timeline": "2 weeks",
                "cost": "R100K",
                "impact": "95% community trust"
            },
            {
                "action": "Satellite Data Integration",
                "rationale": "Unique competitive advantage",
                "timeline": "4 weeks", 
                "cost": "R500K",
                "impact": "40% accuracy improvement"
            },
            {
                "action": "Mobile-First Development",
                "rationale": "80% of African users are mobile-first",
                "timeline": "8 weeks",
                "cost": "R2M",
                "impact": "5x user base expansion"
            }
        ]
        
        for action in high_priority:
            st.markdown(f"""
            <div class="recommendation-card">
                <strong>{action['action']}</strong><br>
                <em>{action['rationale']}</em><br>
                <small>Timeline: {action['timeline']} | Cost: {action['cost']} | Impact: {action['impact']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("💰 Funding Strategy")
        
        funding_rounds = [
            {
                "round": "Pre-Seed (Current)",
                "amount": "R5M",
                "investors": "Angel investors, family offices",
                "use": "Product development, pilot customers",
                "timeline": "Completed"
            },
            {
                "round": "Seed Round",
                "amount": "R20M",
                "investors": "African VCs, development finance",
                "use": "Market expansion, team building",
                "timeline": "Next 6 months"
            },
            {
                "round": "Series A",
                "amount": "R100M",
                "investors": "International VCs, impact funds",
                "use": "Multi-country expansion, AI development",
                "timeline": "18 months"
            }
        ]
        
        for round_info in funding_rounds:
            with st.expander(f"{round_info['round']}: {round_info['amount']}"):
                st.markdown(f"**Investors:** {round_info['investors']}")
                st.markdown(f"**Use of Funds:** {round_info['use']}")
                st.markdown(f"**Timeline:** {round_info['timeline']}")
    
    # Risk mitigation
    st.subheader("⚠️ Risk Mitigation Strategy")
    
    risks = [
        {
            "risk": "Competition from Global ESG Platforms",
            "probability": "High",
            "impact": "High",
            "mitigation": "Focus on Ubuntu authenticity and African-specific features"
        },
        {
            "risk": "Regulatory Changes",
            "probability": "Medium",
            "impact": "Medium",
            "mitigation": "Flexible compliance engine, regulatory partnerships"
        },
        {
            "risk": "Economic Downturn",
            "probability": "Medium",
            "impact": "High",
            "mitigation": "Essential service positioning, government partnerships"
        }
    ]
    
    risk_df = pd.DataFrame(risks)
    st.dataframe(risk_df, use_container_width=True)

# Continue with existing pages but enhanced...
elif page == "📊 Ubuntu ESG Calculator":
    # Enhanced calculator with satellite integration and mobile optimization
    st.header("Ubuntu ESG Calculator - Enhanced Edition")
    st.markdown("**AI-powered scoring with satellite verification and community validation**")
    
    # Add satellite data toggle
    use_satellite = st.checkbox("🛰️ Include Satellite Environmental Data", value=True)
    community_verification = st.checkbox("🤝 Enable Community Verification", value=True)
    
    # Enhanced scoring with new data sources
    with st.form("enhanced_esg_calculator"):
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🌍 Environmental Metrics (Satellite Enhanced)")
            carbon_emissions = st.slider("Carbon Emissions Reduction (%)", 0, 100, 35)
            if use_satellite:
                st.info("🛰️ Satellite verification: +15% accuracy bonus")
                carbon_emissions = min(carbon_emissions + 15, 100)
            
            renewable_energy = st.slider("Renewable Energy Usage (%)", 0, 100, 25)
            water_efficiency = st.slider("Water Efficiency Score", 0, 100, 60)
            waste_reduction = st.slider("Waste Reduction (%)", 0, 100, 40)
            
            st.subheader("🏛️ Governance Metrics")
            board_diversity = st.slider("Board Diversity Score", 0, 100, 65)
            transparency = st.slider("Transparency & Disclosure", 0, 100, 75)
            ethics_score = st.slider("Ethics & Anti-corruption", 0, 100, 80)
        
        with col2:
            st.subheader("👥 Social Metrics (Community Verified)")
            employee_wellbeing = st.slider("Employee Wellbeing", 0, 100, 70)
            community_engagement = st.slider("Community Engagement", 0, 100, 85)
            if community_verification:
                st.info("🤝 Community verification: +10% trust bonus")
                community_engagement = min(community_engagement + 10, 100)
            
            diversity_inclusion = st.slider("Diversity & Inclusion", 0, 100, 68)
            local_employment = st.slider("Local Employment (%)", 0, 100, 75)
            
            st.subheader("🤝 Enhanced Ubuntu Index")
            local_procurement = st.slider("Local Procurement (%)", 0, 100, 45)
            cultural_preservation = st.slider("Cultural Preservation", 0, 100, 60)
            indigenous_knowledge = st.slider("Indigenous Knowledge Integration", 0, 100, 55)
            community_investment = st.slider("Community Investment (% of revenue)", 0, 10, 2)
            traditional_leader_endorsement = st.checkbox("Traditional Leader Endorsement", value=False)
        
        submitted = st.form_submit_button("🧮 Calculate Enhanced Ubuntu ESG Score", type="primary")
    
    if submitted:
        # Enhanced calculation with bonuses
        satellite_bonus = 5 if use_satellite else 0
        community_bonus = 8 if community_verification else 0
        traditional_bonus = 12 if traditional_leader_endorsement else 0
        
        env_score = (carbon_emissions * 0.3 + renewable_energy * 0.25 + 
                    water_efficiency * 0.25 + waste_reduction * 0.2) + satellite_bonus
        
        social_score = (employee_wellbeing * 0.25 + community_engagement * 0.25 + 
                       diversity_inclusion * 0.25 + local_employment * 0.25) + community_bonus
        
        governance_score = (board_diversity * 0.35 + transparency * 0.35 + ethics_score * 0.3)
        
        ubuntu_score = (local_procurement * 0.25 + cultural_preservation * 0.2 + 
                       indigenous_knowledge * 0.2 + (community_investment * 10) * 0.2 + 
                       community_engagement * 0.15) + traditional_bonus
        
        # Overall ESG score with enhanced weighting
        overall_score = (env_score * 0.25 + social_score * 0.35 + 
                        governance_score * 0.25 + ubuntu_score * 0.15)
        
        # Cap scores at 100
        env_score = min(env_score, 100)
        social_score = min(social_score, 100)
        governance_score = min(governance_score, 100)
        ubuntu_score = min(ubuntu_score, 100)
        overall_score = min(overall_score, 100)
        
        # Enhanced results display
        st.success("✅ Enhanced Ubuntu ESG Score Calculated with AI & Community Verification!")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Overall ESG Score", f"{overall_score:.1f}/100")
            st.metric("Environmental", f"{env_score:.1f}/100")
            st.metric("Social", f"{social_score:.1f}/100")
        
        with col2:
            st.metric("Governance", f"{governance_score:.1f}/100")
            st.metric("Enhanced Ubuntu Index™", f"{ubuntu_score:.1f}/100")
            
            # Enhanced ESG Rating
            if overall_score >= 85:
                rating = "AAA"
                color = "green"
            elif overall_score >= 75:
                rating = "AA"
                color = "lightgreen"
            elif overall_score >= 65:
                rating = "A"
                color = "orange"
            else:
                rating = "BBB"
                color = "red"
            
            st.markdown(f"<h3 style='color: {color};'>ESG Rating: {rating}</h3>", unsafe_allow_html=True)
        
        with col3:
            # Enhanced Ubuntu Rating
            if ubuntu_score >= 90:
                ubuntu_rating = "Ubuntu Master"
            elif ubuntu_score >= 80:
                ubuntu_rating = "Ubuntu Champion"
            elif ubuntu_score >= 65:
                ubuntu_rating = "Ubuntu Advocate"
            elif ubuntu_score >= 50:
                ubuntu_rating = "Ubuntu Aligned"
            else:
                ubuntu_rating = "Ubuntu Developing"
            
            st.markdown(f"<h3 style='color: #1c7e57;'>{ubuntu_rating}</h3>", unsafe_allow_html=True)
            
            # Enhancement bonuses
            if satellite_bonus > 0:
                st.success(f"🛰️ +{satellite_bonus} Satellite Bonus")
            if community_bonus > 0:
                st.success(f"🤝 +{community_bonus} Community Bonus")
            if traditional_bonus > 0:
                st.success(f"👑 +{traditional_bonus} Traditional Leader Bonus")

# Enhanced subscription plans
elif page == "💰 Subscription Plans":
    
    st.header("ESGx.Africa Enhanced Subscription Plans")
    st.markdown("**Choose the plan that fits your organization's enhanced ESG needs**")
    
    # Enhanced plans with new features
    enhanced_plans = {
        "Community Free": {
            "price_monthly": "R0",
            "price_annual": "R0", 
            "features": ["Ubuntu Index™", "SMS input", "3 reports/month", "Basic ESG scoring", "Mobile app access"],
            "new_features": ["WhatsApp bot", "Community network"],
            "max_reports": 3,
            "ai_agents": 0,
            "satellite_data": False,
            "api_calls": 100,
            "color": "#6c757d"
        },
        "Ubuntu Starter": {
            "price_monthly": "R2,500",
            "price_annual": "R25,000",
            "features": ["Core ESG KPIs", "ESG wizard", "Email support", "1 AI agent", "50 reports/month"],
            "new_features": ["Mobile app premium", "Basic satellite data", "Community mentorship"],
            "max_reports": 50,
            "ai_agents": 1,
            "satellite_data": True,
            "api_calls": 5000,
            "color": "#17a2b8"
        },
        "Growth Pro": {
            "price_monthly": "R15,000", 
            "price_annual": "R150,000",
            "features": ["2 AI agents", "JSE compliance", "ESGx metrics", "500 reports/month", "Priority support"],
            "new_features": ["Full satellite integration", "API marketplace", "Investment tracker", "Traditional leader verification"],
            "max_reports": 500,
            "ai_agents": 2,
            "satellite_data": True,
            "api_calls": 50000,
            "color": "#1c7e57",
            "featured": True
        },
        "Enterprise ESG": {
            "price_monthly": "R75,000",
            "price_annual": "R750,000", 
            "features": ["All AI agents", "API access", "Custom reporting", "Unlimited reports", "Dedicated support"],
            "new_features": ["Real-time satellite monitoring", "Full API access", "White-label options", "Custom integrations"],
            "max_reports": "Unlimited",
            "ai_agents": 5,
            "satellite_data": True,
            "api_calls": "Unlimited",
            "color": "#dc3545"
        },
        "Enterprise+": {
            "price_monthly": "Custom",
            "price_annual": "Avg R1.5M",
            "features": ["On-premise deployment", "White-labeling", "Dedicated AI", "Custom integrations"],
            "new_features": ["Private satellite feeds", "Custom AI training", "Government partnerships", "Traditional council integration"],
            "max_reports": "Unlimited", 
            "ai_agents": "Unlimited",
            "satellite_data": True,
            "api_calls": "Unlimited",
            "color": "#6f42c1"
        }
    }
    
    cols = st.columns(len(enhanced_plans))
    
    for i, (plan_name, plan_data) in enumerate(enhanced_plans.items()):
        with cols[i]:
            card_class = "subscription-card featured-card" if plan_data.get("featured") else "subscription-card"
            
            st.markdown(f"""
            <div class="{card_class}">
                <h3 style="color: {plan_data['color']};">{plan_name}</h3>
                <div style="font-size: 1.5rem; font-weight: bold;">
                    {plan_data['price_monthly']}/month
                </div>
                <div style="color: #666; margin-bottom: 1rem;">
                    {plan_data['price_annual']}/year
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Core Features:**")
            for feature in plan_data['features']:
                st.markdown(f"✅ {feature}")
                
            st.markdown("**🚀 New Features:**")
            for feature in plan_data['new_features']:
                st.markdown(f"🆕 {feature}")
            
            st.markdown(f"📊 **Reports/month:** {plan_data['max_reports']}")
            st.markdown(f"🤖 **AI Agents:** {plan_data['ai_agents']}")
            st.markdown(f"🛰️ **Satellite Data:** {'✅' if plan_data['satellite_data'] else '❌'}")
            st.markdown(f"🔗 **API Calls:** {plan_data['api_calls']}")
            
            if plan_data.get("featured"):
                st.success("🌟 Most Popular - Enhanced Edition")
            
            if st.button(f"Choose {plan_name}", key=f"enhanced_btn_{i}"):
                st.balloons()
                st.success(f"🎉 Welcome to {plan_name}! Enhanced features activated.")

# Continue with other enhanced pages...
else:
    # For remaining pages, show enhanced versions of existing content
    exec(open('esgx_africa_demo.py').read().split('# Continue with existing pages')[0])

# Enhanced Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 20px;'>
        <h3>🌍 ESGx.Africa™ Enhanced Platform</h3>
        <p><strong>Powered by Ubuntu Philosophy | Enhanced with AI & Satellite Data | Made for Africa</strong></p>
        <p>🚀 <strong>New Features:</strong> Satellite monitoring | Mobile-first | Community verification | Investment tracking</p>
        <p>🤝 <strong>Partnerships:</strong> African Development Bank | Traditional Leaders Council | NASA Earth Observatory</p>
        <p>📱 <strong>Available on:</strong> Web | iOS | Android | WhatsApp | SMS</p>
        <hr>
        <p style='font-size: 0.9rem;'>
            <strong>Ubuntu Philosophy:</strong> "I am because we are" - Our technology serves communities, 
            our communities strengthen our technology. Together, we build Africa's sustainable future.
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)