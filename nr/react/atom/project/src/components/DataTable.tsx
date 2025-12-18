import React, { useState, useMemo } from 'react';
import { ArrowUpDown, Download, Settings2, Eye, EyeOff, Check, X, Filter } from 'lucide-react';
import { User, Column } from '../types';

interface DataTableProps {
  data: User[];
}

interface ColumnCategory {
  name: string;
  columns: Column[];
}

const DataTable: React.FC<DataTableProps> = ({ data }) => {
  const [columns, setColumns] = useState<Column[]>([
    { key: 'name', label: 'Name', visible: true, category: 'Basic Info' },
    { key: 'email', label: 'Email', visible: true, category: 'Basic Info' },
    { key: 'role', label: 'Role', visible: true, category: 'Basic Info' },
    { key: 'department', label: 'Department', visible: true, category: 'Organization' },
    { key: 'status', label: 'Status', visible: true, category: 'Basic Info' },
    { key: 'location', label: 'Location', visible: true, category: 'Organization' },
    { key: 'hireDate', label: 'Hire Date', visible: true, category: 'Employment' },
    { key: 'performanceScore', label: 'Performance', visible: true, category: 'Performance' },
    { key: 'projectCount', label: 'Projects', visible: true, category: 'Performance' },
    { key: 'teamSize', label: 'Team Size', visible: true, category: 'Organization' },
    { key: 'lastActive', label: 'Last Active', visible: false, category: 'Activity' },
    { key: 'phoneNumber', label: 'Phone', visible: false, category: 'Contact' },
    { key: 'salary', label: 'Salary', visible: false, category: 'Employment' },
    { key: 'certifications', label: 'Certifications', visible: false, category: 'Professional' },
    { key: 'reportsTo', label: 'Reports To', visible: false, category: 'Organization' },
    { key: 'lastPromotion', label: 'Last Promotion', visible: false, category: 'Employment' },
    { key: 'workSchedule', label: 'Work Schedule', visible: false, category: 'Employment' },
    { key: 'vacationDays', label: 'Vacation Days', visible: false, category: 'Employment' },
    { key: 'trainingHours', label: 'Training Hours', visible: false, category: 'Professional' },
    { key: 'id', label: 'ID', visible: false, category: 'System' },
  ]);

  const [sortConfig, setSortConfig] = useState<{
    key: keyof User | null;
    direction: 'asc' | 'desc';
  }>({ key: null, direction: 'asc' });

  const [filterText, setFilterText] = useState('');
  const [roleFilter, setRoleFilter] = useState<string>('');
  const [departmentFilter, setDepartmentFilter] = useState<string>('');
  const [showColumnSelector, setShowColumnSelector] = useState(false);

  const uniqueRoles = useMemo(() => {
    return Array.from(new Set(data.map(item => item.role))).sort();
  }, [data]);

  const uniqueDepartments = useMemo(() => {
    return Array.from(new Set(data.map(item => item.department))).sort();
  }, [data]);

  const columnCategories = useMemo(() => {
    const categories = columns.reduce((acc, column) => {
      const category = acc.find(c => c.name === column.category);
      if (category) {
        category.columns.push(column);
      } else {
        acc.push({ name: column.category, columns: [column] });
      }
      return acc;
    }, [] as ColumnCategory[]);

    return categories.sort((a, b) => a.name.localeCompare(b.name));
  }, [columns]);

  const handleSort = (key: keyof User) => {
    setSortConfig({
      key,
      direction:
        sortConfig.key === key && sortConfig.direction === 'asc' ? 'desc' : 'asc',
    });
  };

  const sortedAndFilteredData = useMemo(() => {
    let filteredData = [...data];

    if (filterText) {
      filteredData = filteredData.filter((item) =>
        Object.values(item).some((value) =>
          value.toString().toLowerCase().includes(filterText.toLowerCase())
        )
      );
    }

    if (roleFilter) {
      filteredData = filteredData.filter(item => item.role === roleFilter);
    }

    if (departmentFilter) {
      filteredData = filteredData.filter(item => item.department === departmentFilter);
    }

    if (sortConfig.key) {
      filteredData.sort((a, b) => {
        const aValue = a[sortConfig.key!];
        const bValue = b[sortConfig.key!];
        if (aValue < bValue) return sortConfig.direction === 'asc' ? -1 : 1;
        if (aValue > bValue) return sortConfig.direction === 'asc' ? 1 : -1;
        return 0;
      });
    }

    return filteredData;
  }, [data, filterText, roleFilter, departmentFilter, sortConfig]);

  const toggleColumn = (key: keyof User) => {
    setColumns(
      columns.map((col) =>
        col.key === key ? { ...col, visible: !col.visible } : col
      )
    );
  };

  const toggleAllInCategory = (categoryName: string, visible: boolean) => {
    setColumns(
      columns.map((col) =>
        col.category === categoryName ? { ...col, visible } : col
      )
    );
  };

  const exportToCSV = () => {
    const visibleColumns = columns.filter((col) => col.visible);
    const headers = visibleColumns.map((col) => col.label).join(',');
    const rows = sortedAndFilteredData
      .map((row) =>
        visibleColumns
          .map((col) => row[col.key])
          .map((cell) => `"${cell}"`)
          .join(',')
      )
      .join('\n');
    
    const csv = `${headers}\n${rows}`;
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'table-export.csv';
    a.click();
    window.URL.revokeObjectURL(url);
  };

  return (
    <div className="w-full bg-white rounded-lg shadow-lg overflow-hidden">
      <div className="p-4 border-b border-gray-200 flex flex-col space-y-4 bg-white sticky top-0 z-10">
        <div className="flex justify-between items-center">
          <div className="flex items-center space-x-4">
            <input
              type="text"
              placeholder="Filter table..."
              className="px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={filterText}
              onChange={(e) => setFilterText(e.target.value)}
            />
            <button
              onClick={() => setShowColumnSelector(true)}
              className="p-2 rounded-lg transition-colors hover:bg-gray-100"
              title="Column Settings"
            >
              <Settings2 className="w-5 h-5" />
            </button>
          </div>
          <button
            onClick={exportToCSV}
            className="flex items-center space-x-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            <Download className="w-4 h-4" />
            <span>Export CSV</span>
          </button>
        </div>

        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-2">
            <Filter className="w-4 h-4 text-gray-500" />
            <select
              value={roleFilter}
              onChange={(e) => setRoleFilter(e.target.value)}
              className="px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">All Roles</option>
              {uniqueRoles.map(role => (
                <option key={role} value={role}>{role}</option>
              ))}
            </select>
          </div>
          <div className="flex items-center space-x-2">
            <Filter className="w-4 h-4 text-gray-500" />
            <select
              value={departmentFilter}
              onChange={(e) => setDepartmentFilter(e.target.value)}
              className="px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">All Departments</option>
              {uniqueDepartments.map(dept => (
                <option key={dept} value={dept}>{dept}</option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* Modal Overlay */}
      {showColumnSelector && (
        <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center">
          {/* Modal Content */}
          <div className="bg-white rounded-xl shadow-2xl w-full max-w-4xl max-h-[90vh] overflow-hidden">
            {/* Modal Header */}
            <div className="px-6 py-4 border-b border-gray-200 flex justify-between items-center bg-gray-50">
              <h3 className="text-xl font-semibold text-gray-900">Customize Columns</h3>
              <button
                onClick={() => setShowColumnSelector(false)}
                className="p-2 hover:bg-gray-200 rounded-full transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Modal Body */}
            <div className="p-6 overflow-y-auto max-h-[calc(90vh-120px)]">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {columnCategories.map((category) => (
                  <div
                    key={category.name}
                    className="bg-white p-4 rounded-lg shadow-sm border border-gray-200"
                  >
                    <div className="flex items-center justify-between mb-3">
                      <h4 className="font-medium text-gray-900">{category.name}</h4>
                      <div className="flex space-x-2">
                        <button
                          onClick={() => toggleAllInCategory(category.name, true)}
                          className="p-1 hover:bg-blue-50 rounded text-blue-600"
                          title="Show all"
                        >
                          <Eye className="w-4 h-4" />
                        </button>
                        <button
                          onClick={() => toggleAllInCategory(category.name, false)}
                          className="p-1 hover:bg-blue-50 rounded text-blue-600"
                          title="Hide all"
                        >
                          <EyeOff className="w-4 h-4" />
                        </button>
                      </div>
                    </div>
                    <div className="space-y-2">
                      {category.columns.map((column) => (
                        <label
                          key={column.key}
                          className="flex items-center justify-between p-2 hover:bg-gray-50 rounded cursor-pointer group"
                        >
                          <span className="text-sm text-gray-700">{column.label}</span>
                          <button
                            onClick={() => toggleColumn(column.key)}
                            className={`w-8 h-8 flex items-center justify-center rounded-full transition-colors ${
                              column.visible
                                ? 'bg-blue-100 text-blue-600'
                                : 'bg-gray-100 text-gray-400 group-hover:bg-gray-200'
                            }`}
                          >
                            <Check className={`w-4 h-4 ${column.visible ? 'opacity-100' : 'opacity-0 group-hover:opacity-50'}`} />
                          </button>
                        </label>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Modal Footer */}
            <div className="px-6 py-4 border-t border-gray-200 bg-gray-50">
              <button
                onClick={() => setShowColumnSelector(false)}
                className="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
              >
                Done
              </button>
            </div>
          </div>
        </div>
      )}

      <div className="overflow-x-auto">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              {columns
                .filter((col) => col.visible)
                .map((column) => (
                  <th
                    key={column.key}
                    className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                    onClick={() => handleSort(column.key)}
                  >
                    <div className="flex items-center space-x-1">
                      <span>{column.label}</span>
                      <ArrowUpDown className="w-4 h-4" />
                    </div>
                  </th>
                ))}
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {sortedAndFilteredData.map((row) => (
              <tr key={row.id} className="hover:bg-gray-50">
                {columns
                  .filter((col) => col.visible)
                  .map((column) => (
                    <td
                      key={`${row.id}-${column.key}`}
                      className="px-6 py-4 whitespace-nowrap text-sm text-gray-900"
                    >
                      {row[column.key]}
                    </td>
                  ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default DataTable;