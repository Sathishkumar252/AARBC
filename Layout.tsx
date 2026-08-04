import { Outlet, Link, useLocation } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import {
  LayoutDashboard,
  Briefcase,
  AlertTriangle,
  BarChart3,
  LogOut,
  Shield,
  ListOrdered,
} from 'lucide-react'

export default function Layout() {
  const { user, logout } = useAuth()
  const location = useLocation()

  const navItems = [
    { path: '/', label: 'Dashboard', icon: LayoutDashboard },
    { path: '/cases', label: 'Cases', icon: Briefcase },
    { path: '/priority', label: 'Priority Queue', icon: ListOrdered },
    { path: '/alerts', label: 'Alerts', icon: AlertTriangle },
    { path: '/analytics', label: 'Analytics', icon: BarChart3 },
  ]

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {/* Sidebar */}
      <aside className="w-64 bg-judicial-900 text-white flex flex-col fixed h-full">
        <div className="p-6 border-b border-judicial-800">
          <div className="flex items-center gap-3">
            <Shield className="w-8 h-8 text-judicial-400" />
            <div>
              <h1 className="text-xl font-bold">DocketClear</h1>
              <p className="text-xs text-judicial-400">AI for Justice</p>
            </div>
          </div>
        </div>

        <nav className="flex-1 p-4 space-y-1">
          {navItems.map((item) => {
            const Icon = item.icon
            const isActive = location.pathname === item.path
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                  isActive
                    ? 'bg-judicial-700 text-white'
                    : 'text-judicial-300 hover:bg-judicial-800 hover:text-white'
                }`}
              >
                <Icon className="w-5 h-5" />
                <span className="font-medium">{item.label}</span>
              </Link>
            )
          })}
        </nav>

        <div className="p-4 border-t border-judicial-800">
          <div className="mb-3 px-4">
            <p className="text-sm font-medium text-white">{user?.full_name}</p>
            <p className="text-xs text-judicial-400 capitalize">{user?.role}</p>
          </div>
          <button
            onClick={logout}
            className="flex items-center gap-3 px-4 py-2 text-judicial-300 hover:text-white w-full rounded-lg hover:bg-judicial-800 transition-colors"
          >
            <LogOut className="w-5 h-5" />
            <span>Logout</span>
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 ml-64 p-8">
        <Outlet />
      </main>
    </div>
  )
}
