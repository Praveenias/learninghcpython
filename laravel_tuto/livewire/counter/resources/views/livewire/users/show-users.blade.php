<div class="container pt-4">
        
    <table class="table table-dark table-striped" >
        <thead>
            <tr>
                <th scope="col">Id</th>
                <th scope="col">Name</th>
                <th scope="col">Email</th>
                <th scope="col">Password</th>
                <th scope="col">Handle</th>
            </tr>
        </thead>
        <tbody>
        @forelse($users as $user)
            <tr>
                <td>{{$user->id}}</td>
                <td>{{$user->name}}</td>
                <td>{{$user->email}}</td>
                <td>{{$user->password}}</td>
                <td>
                    <a href="{{ route('users.edit',$user)}}" class="btn btn-primary">Edit</a>
                    <button class="btn btn-danger" wire:click="deleteuser({{$user->id}})" onclick="return confirm('Delete COnfirmation?') || event.stopImmediatePropagation()">Delete</button>
                </td>
            </tr>
        @empty
        <tr>
            <td class="px-6 py-4 text-sm" colspan="3">
                No products were found.
            </td>
        </tr>
        @endforelse
        </tbody>
    </table>
    {{ $users->links() }} 
</div>
