def edit_author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)  # ✅ Corrected request.POST
        if form.is_valid():
            form.save()
            return redirect('authors_page')
    else:
        form = AuthorForm(instance=author)  # ✅ Moved this block to handle non-POST requests.
    return render(request, 'edit_author.html', {'form': form})  # ✅ Corrected dictionary syntax.
