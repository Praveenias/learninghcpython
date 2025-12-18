<?php

namespace App\Livewire\Users;

use App\Models\User;
use Livewire\Component;
use Livewire\WithPagination;

class ShowUsers extends Component
{
    use WithPagination; 

    public function deleteuser(int $userId){
        sleep(2);
        User::where('id', $userId)->delete();
    }
    public function render()
    {
        return view('livewire.users.show-users',[
            'users'=>User::paginate(10),
        ]);
    }
}
