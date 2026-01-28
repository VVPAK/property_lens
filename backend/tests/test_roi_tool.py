import pytest
from app.services.agent.tools import ROICalculatorTool

def test_roi_calculator_gross_roi():
    tool = ROICalculatorTool()
    # Price: 1,000,000, Rent: 80,000 -> Gross ROI should be 8.0%
    result = tool._run(price=1000000, annual_rent=80000)
    assert result["gross_roi_percent"] == 8.0

def test_roi_calculator_net_roi():
    tool = ROICalculatorTool()
    # Price: 1,000,000, Rent: 80,000, Service Charges: 15,000
    # Net Income: 65,000 -> Net ROI: 6.5%
    result = tool._run(price=1000000, annual_rent=80000, service_charges=15000)
    assert result["net_income"] == 65000
    assert result["net_roi_percent"] == 6.5

def test_roi_calculator_zero_price_error():
    tool = ROICalculatorTool()
    with pytest.raises(ZeroDivisionError):
        tool._run(price=0, annual_rent=50000)
