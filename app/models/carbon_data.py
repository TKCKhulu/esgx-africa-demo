"""
ESGx.Africa Carbon Data Model
Carbon accounting and emissions tracking for African organizations
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

from app.db.session import Base

class CarbonData(Base):
    """Carbon data model for emissions tracking and carbon accounting"""
    __tablename__ = "carbon_data"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relationships
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Reporting period
    reporting_year = Column(Integer, nullable=False)
    reporting_period_start = Column(DateTime, nullable=False)
    reporting_period_end = Column(DateTime, nullable=False)
    
    # Scope 1 Emissions (Direct emissions)
    scope1_total = Column(Float, default=0.0)  # tCO2e
    scope1_stationary_combustion = Column(Float, default=0.0)
    scope1_mobile_combustion = Column(Float, default=0.0)
    scope1_fugitive_emissions = Column(Float, default=0.0)
    scope1_process_emissions = Column(Float, default=0.0)
    
    # Scope 2 Emissions (Indirect energy emissions)
    scope2_total = Column(Float, default=0.0)  # tCO2e
    scope2_electricity_consumption = Column(Float, default=0.0)
    scope2_heating_cooling = Column(Float, default=0.0)
    scope2_steam = Column(Float, default=0.0)
    
    # Scope 3 Emissions (Other indirect emissions)
    scope3_total = Column(Float, default=0.0)  # tCO2e
    scope3_business_travel = Column(Float, default=0.0)
    scope3_employee_commuting = Column(Float, default=0.0)
    scope3_waste = Column(Float, default=0.0)
    scope3_water = Column(Float, default=0.0)
    scope3_purchased_goods = Column(Float, default=0.0)
    scope3_upstream_transport = Column(Float, default=0.0)
    scope3_downstream_transport = Column(Float, default=0.0)
    
    # Total emissions
    total_emissions = Column(Float, nullable=False)  # tCO2e
    
    # African-specific emissions sources
    deforestation_emissions = Column(Float, default=0.0)  # Land use change
    agriculture_emissions = Column(Float, default=0.0)  # Agricultural activities
    mining_emissions = Column(Float, default=0.0)  # Mining-specific emissions
    generator_emissions = Column(Float, default=0.0)  # Backup generators (common in Africa)
    cooking_fuel_emissions = Column(Float, default=0.0)  # Traditional cooking fuels
    
    # Energy consumption data
    electricity_consumption_kwh = Column(Float, default=0.0)
    renewable_energy_percentage = Column(Float, default=0.0)
    solar_energy_kwh = Column(Float, default=0.0)
    wind_energy_kwh = Column(Float, default=0.0)
    hydro_energy_kwh = Column(Float, default=0.0)
    
    # Carbon offsets and mitigation
    carbon_offsets_purchased = Column(Float, default=0.0)  # tCO2e
    offset_projects = Column(JSON)  # Details of offset projects
    tree_planting_count = Column(Integer, default=0)
    conservation_area_hectares = Column(Float, default=0.0)
    
    # African carbon market integration
    voluntary_carbon_credits = Column(Float, default=0.0)
    compliance_carbon_credits = Column(Float, default=0.0)
    african_carbon_exchange_participation = Column(Boolean, default=False)
    
    # Intensity metrics
    emissions_per_employee = Column(Float)  # tCO2e per employee
    emissions_per_revenue = Column(Float)  # tCO2e per currency unit
    emissions_per_product = Column(Float)  # tCO2e per product unit
    
    # Data quality and verification
    data_quality_rating = Column(String)  # high, medium, low
    verification_status = Column(String)  # verified, self-reported, estimated
    verification_body = Column(String)
    verification_date = Column(DateTime)
    
    # Methodology and standards
    calculation_methodology = Column(String)  # GHG Protocol, ISO 14064, etc.
    emission_factors_source = Column(String)
    uncertainty_percentage = Column(Float)
    
    # Targets and commitments
    reduction_target_percentage = Column(Float)  # % reduction target
    target_year = Column(Integer)
    net_zero_commitment = Column(Boolean, default=False)
    net_zero_target_year = Column(Integer)
    
    # African context and adaptation
    climate_adaptation_investments = Column(Float, default=0.0)  # Investment in adaptation
    water_stress_region = Column(Boolean, default=False)
    drought_resilience_measures = Column(JSON)
    
    # Supporting data
    activity_data = Column(JSON)  # Detailed activity data
    emission_factors = Column(JSON)  # Emission factors used
    assumptions = Column(JSON)  # Calculation assumptions
    
    # AI-generated insights
    ai_recommendations = Column(JSON)  # AI recommendations for reduction
    hotspot_analysis = Column(JSON)  # Emission hotspots identified
    benchmark_comparison = Column(JSON)  # Industry benchmark comparison
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    organization = relationship("Organization", back_populates="carbon_data")
    user = relationship("User")
    
    def __repr__(self):
        return f"<CarbonData(org_id={self.organization_id}, year={self.reporting_year}, total={self.total_emissions})>"
    
    @property
    def carbon_intensity_class(self) -> str:
        """Classify carbon intensity"""
        if self.emissions_per_employee is None:
            return "Unknown"
        
        if self.emissions_per_employee < 5:
            return "Low"
        elif self.emissions_per_employee < 15:
            return "Medium"
        elif self.emissions_per_employee < 30:
            return "High"
        else:
            return "Very High"
    
    @property
    def scope_breakdown_percentage(self) -> dict:
        """Get percentage breakdown by scope"""
        if self.total_emissions == 0:
            return {"scope1": 0, "scope2": 0, "scope3": 0}
        
        return {
            "scope1": round((self.scope1_total / self.total_emissions) * 100, 1),
            "scope2": round((self.scope2_total / self.total_emissions) * 100, 1),
            "scope3": round((self.scope3_total / self.total_emissions) * 100, 1)
        }
    
    @property
    def is_net_zero_aligned(self) -> bool:
        """Check if emissions trajectory aligns with net zero target"""
        if not self.net_zero_target_year or not self.reduction_target_percentage:
            return False
        
        # Simplified net zero alignment check
        current_year = datetime.now().year
        years_to_target = self.net_zero_target_year - current_year
        required_annual_reduction = self.reduction_target_percentage / years_to_target if years_to_target > 0 else 0
        
        # Check if reduction rate is sufficient (simplified)
        return required_annual_reduction <= 10  # Max 10% per year is realistic
    
    def calculate_african_context_score(self) -> float:
        """Calculate African context score based on local considerations"""
        score = 0.0
        
        # Renewable energy usage
        if self.renewable_energy_percentage > 50:
            score += 25
        elif self.renewable_energy_percentage > 25:
            score += 15
        elif self.renewable_energy_percentage > 10:
            score += 10
        
        # Carbon offset participation
        if self.carbon_offsets_purchased > 0:
            score += 20
        
        # African carbon market participation
        if self.african_carbon_exchange_participation:
            score += 15
        
        # Tree planting and conservation
        if self.tree_planting_count > 1000:
            score += 20
        elif self.tree_planting_count > 100:
            score += 10
        
        # Climate adaptation investments
        if self.climate_adaptation_investments > 0:
            score += 20
        
        return min(score, 100.0)  # Cap at 100