import React, { useState, useEffect } from 'react';
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
} from 'recharts';
import { Filter, Calendar, Users, Tag, BarChart3, PieChart as PieChartIcon, Settings, ChevronDown, Building2, Package2 } from 'lucide-react';
import { Navigation } from './Navigation';
import { Loader } from './common/Loader';
import { getChartData, getCustomernameFromLevel, getProductNameFromCustomer } from '../api/auth';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8', '#82ca9d'];

const levelOptions = [
  { key: '2', value: 'Division' },
  { key: '3', value: 'Business Unit' }
];

const filters = [
  {
    id: 'proactive_analysis_obs',
    name: 'Proactive Analysis',
    icon: Calendar,
    options: ['Yes','No']
  },
  {
    id: 'power_type',
    name: 'Power Type',
    icon: Tag,
    options: ['Active','Passive']
  },
  {
    id: 'risk',
    name: 'Risk',
    icon: Users,
    options: ['HiRisk','MediumRisk','LowRisk','NoRisk']
  },
  {
    id: 'lifecycle_status',
    name: 'LifeCycle Status',
    icon: BarChart3,
    options: ['Active', 'EOL', 'NRND', 'LTB', 'Unconfirmed']
  },
  {
    id: 'sup_risk_group',
    name: 'Risk Group',
    icon: PieChartIcon,
    options: ['Sourcing','Design','NoRisk']
  },
  {
    id: 'bom_type',
    name: 'Bom Type',
    icon: Filter,
    options: ['Production','new_product_development','Obsolete','Service','Redesign']
  },
  {
    id: 'part_category',
    name: 'Part Category',
    icon: Settings,
    options: ['electrical & electronics', 'electro_mechanical', 'mechanical', 'pcb', 'unconfirmed']
  }
];

interface ChartData {
  name: string;
  value: number;
}

interface ChartCardProps {
  title: string;
  data: ChartData[];
  isLoading: boolean;
}

const ChartCard: React.FC<ChartCardProps> = ({ title, data, isLoading }) => (
  <div className="bg-white rounded-lg shadow-sm p-6">
    <h3 className="text-lg font-semibold text-gray-700 mb-6">{title}</h3>
    <div className="h-[250px] relative">
      {isLoading ? (
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="animate-spin rounded-full h-8 w-8 border-4 border-indigo-500 border-t-transparent"></div>
        </div>
      ) : (
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={data}
              cx="50%"
              cy="50%"
              fill="#8884d8"
              paddingAngle={5}
              dataKey="value"
              label={({ name, percent }) => `${name} (${(percent * 100).toFixed(0)}%)`}
            >
              {data.map((_, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      )}
    </div>
  </div>
);

export function Dashboard() {
  const [selectedLevel, setSelectedLevel] = useState<string>('');
  const [customerOptions, setCustomerOptions] = useState<Array<{id: string, display_name: string}>>([]);
  const [productOptions, setProductOptions] = useState<Array<{id: string, product_name: string}>>([]);
  const [selectedCustomer, setSelectedCustomer] = useState<string>('');
  const [selectedProduct, setSelectedProduct] = useState<string>('');
  const [openDropdown, setOpenDropdown] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [chartData, setChartData] = useState<Record<string, ChartData[]>>({});

  const fetchCustomers = async (level: string) => {
    // console.log(level);
    
    setIsLoading(true);
    try {
      // Simulate API call
      let res;
      res = await getCustomernameFromLevel(level);    
      // console.log(res);
      
      
      // Mock response based on level
      const customerList = res;
      
      setCustomerOptions(customerList);
      setSelectedCustomer('');
      setProductOptions([]);
      setSelectedProduct('');
    } catch (error) {
      console.error('Error fetching customers:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchProducts = async (customerId: string) => {
    
    setIsLoading(true);
    try {
      let res;
      res = await getProductNameFromCustomer(customerId);
            
      setProductOptions(res);
      setSelectedProduct('');
    } catch (error) {
      console.error('Error fetching products:', error);
    } finally {
      setIsLoading(false);
    }
  };
  const transformDataToChartFormat = (data: Record<string, any>, field: string): ChartData[] => {
    if (!data[field] || typeof data[field] !== 'object') return [];
    
    // Transform object data to ChartData format
    return Object.entries(data[field]).map(([name, value]) => ({
      name,
      value: typeof value === 'number' ? value : 0
    }));
  };

  const fetchChartData = async () => {
    if (!selectedCustomer || !selectedProduct) {
      alert('Please select both Customer and Product');
      return;
    }

    setIsLoading(true);
    try {
      //await new Promise(resolve => setTimeout(resolve, 1500));
      const response = await getChartData(selectedProduct);
      const attributes = response.data.attributes;
      
      const newChartData = {
        proactiveAnalysis: transformDataToChartFormat(attributes, 'proactive_analysis_obs'),
        powerType: transformDataToChartFormat(attributes, 'power_type'),
        risk: transformDataToChartFormat(attributes, 'risk'),
        lifecycleStatus: transformDataToChartFormat(attributes, 'lifecycle_status'),
        riskGroup: transformDataToChartFormat(attributes, 'sup_risk_group'),
        bomType: transformDataToChartFormat(attributes, 'bom_type'),
        partCategory: transformDataToChartFormat(attributes, 'part_category'),
      };
      console.log(newChartData);
      
      setChartData(newChartData);
    } catch (error) {
      console.error('Error fetching chart data:', error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (selectedLevel) {
      fetchCustomers(selectedLevel);
    }
  }, [selectedLevel]);

  useEffect(() => {
    if (selectedCustomer) {
      fetchProducts(selectedCustomer);
    }
  }, [selectedCustomer]);

  return (
    <div className="min-h-screen bg-gray-50">
      {isLoading && <Loader />}
      <Navigation />
      <div className="w-full px-6 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">OBS Report Dashboard</h1>
          <p className="mt-2 text-gray-600">Comprehensive Performance Metrics</p>
        </div>

        {/* Top Level Filters */}
        <div className="bg-white rounded-lg shadow-sm p-4 mb-4">
          <div className="flex items-center gap-4">
            {/* Level Selection */}
            <div className="flex-1">
              <select
                value={selectedLevel}
                onChange={(e) => setSelectedLevel(e.target.value)}
                className="w-full p-3 rounded-lg border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
              >
                <option value="">Select Level</option>
                {levelOptions.map(option => (
                  <option key={option.key} value={option.key}>{option.value}</option>
                ))}
              </select>
            </div>

            {/* Customer Selection */}
            <div className="flex-1">
              <select
                value={selectedCustomer}
                onChange={(e) => setSelectedCustomer(e.target.value)}
                disabled={!selectedLevel}
                className="w-full p-3 rounded-lg border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 disabled:bg-gray-100"
              >
                <option value="">Select Customer</option>
                {customerOptions.map(option => (
                  <option key={option.id} value={option.id}>{option.display_name}</option>
                ))}
              </select>
            </div>

            {/* Product Selection */}
            <div className="flex-1">
              <select
                value={selectedProduct}
                onChange={(e) => setSelectedProduct(e.target.value)}
                disabled={!selectedCustomer}
                className="w-full p-3 rounded-lg border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 disabled:bg-gray-100"
              >
                <option value="">Select Product</option>
                {productOptions.map(option => (
                  <option key={option.id} value={option.id}>{option.product_name}</option>
                ))}
              </select>
            </div>

            {/* Fetch Data Button */}
            <button
              onClick={fetchChartData}
              disabled={!selectedProduct}
              className="px-6 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors duration-200 disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center gap-2"
            >
              <BarChart3 className="h-5 w-5" />
              <span>Fetch Data</span>
            </button>
          </div>
        </div>

        {/* Secondary Filters */}
        <div className="bg-white rounded-lg shadow-sm p-4 mb-8">
          <h2 className="text-lg font-semibold text-gray-700 mb-4">Additional Filters</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-7 gap-4">
            {filters.map((filter) => (
              <div key={filter.id} className="relative">
                <button
                  onClick={() => setOpenDropdown(openDropdown === filter.id ? null : filter.id)}
                  className="w-full flex items-center justify-between p-3 rounded-lg border border-gray-200 hover:bg-gray-50"
                >
                  <div className="flex items-center">
                    <filter.icon className="h-5 w-5 mr-2 text-gray-500" />
                    <span className="font-medium text-gray-700">{filter.name}</span>
                  </div>
                  <ChevronDown className="h-4 w-4" />
                </button>
                
                {openDropdown === filter.id && (
                  <div className="absolute z-10 mt-2 w-full bg-white rounded-lg shadow-lg border border-gray-200 py-1">
                    {filter.options.map((option) => (
                      <button
                        key={option}
                        className="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-indigo-50 hover:text-indigo-700"
                      >
                        {option}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Charts Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          <ChartCard title="Part Category" data={chartData.partCategory || []} isLoading={isLoading} />
          <ChartCard title="Lifecycle Status" data={chartData.lifecycleStatus || []} isLoading={isLoading} />
          <ChartCard title="Risk" data={chartData.risk || []} isLoading={isLoading} />
          <ChartCard title="Proactive Analysis" data={chartData.proactiveAnalysis || []} isLoading={isLoading} />
          <ChartCard title="Power Type" data={chartData.powerType || []} isLoading={isLoading} />
          <ChartCard title="Risk Group" data={chartData.riskGroup || []} isLoading={isLoading} />
          <ChartCard title="BOM Type" data={chartData.bomType || []} isLoading={isLoading} />
        </div>
      </div>
    </div>
  );
}