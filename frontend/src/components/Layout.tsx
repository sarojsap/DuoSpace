import { Outlet, NavLink } from 'react-router-dom';
import { MessageCircle, Image, Heart } from 'lucide-react';

export default function Layout() {
  return (
    <div className="flex flex-col h-screen max-w-md mx-auto bg-white shadow-xl overflow-hidden border-x border-slate-100">
      {/* Main Content Area */}
      <main className="flex-1 overflow-y-auto pb-16">
        <Outlet />
      </main>

      {/* Bottom Navigation */}
      <nav className="absolute bottom-0 w-full max-w-md bg-white border-t border-slate-100 flex justify-around items-center h-16 px-4">
        <NavLink to="/chat" className={({ isActive }) => `flex flex-col items-center ${isActive ? 'text-brand' : 'text-slate-400'}`}>
          <MessageCircle size={24} />
          <span className="text-[10px] mt-1 font-medium">Chat</span>
        </NavLink>
        
        <NavLink to="/prompts" className={({ isActive }) => `flex flex-col items-center ${isActive ? 'text-brand' : 'text-slate-400'}`}>
          <Heart size={24} />
          <span className="text-[10px] mt-1 font-medium">Daily</span>
        </NavLink>

        <NavLink to="/timeline" className={({ isActive }) => `flex flex-col items-center ${isActive ? 'text-brand' : 'text-slate-400'}`}>
          <Image size={24} />
          <span className="text-[10px] mt-1 font-medium">Memories</span>
        </NavLink>
      </nav>
    </div>
  );
}